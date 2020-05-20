import socket
import threading
from views_2 import get_top_words
import json
from config import n_workers, n
from queue import Queue
import signal


class MasterWorker:
    def __init__(self):
        self.work_queue = Queue()
        self.work_queue_done = Queue()
        self.n_workers = n_workers
        self.success_download = 0
        self.run()

    def run(self):
        signal.signal(signal.SIGUSR1, self.finish)

        self.thread_connect = threading.Thread(target=self.connect)
        self.thread_connect.start()
        for i in range(self.n_workers):
            worker = threading.Thread(target=self.parse_url, args=(i,))
            worker.start()
        self.thread_send_response = threading.Thread(target=self.send_response)
        self.thread_send_response.start()

    def connect(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('localhost', 5000))
        server_socket.listen()
        server_socket.settimeout(300)
        while True:
            conn, addr = server_socket.accept()
            self.get_data(conn)

    def get_data(self, conn):
        while True:
            request = conn.recv(2 ** 12)
            if not request:
                break
            request = request.decode()
            self.work_queue.put((request, conn))

    def parse_url(self, i):
        while True:
            if not self.work_queue.empty():  # лучше так не делать, лучше лок
                request, conn = self.work_queue.get()
                response = get_top_words(json.loads(request)['data'], n)
                self.work_queue.task_done()
                self.success_download += 1
                print(i)
                self.work_queue_done.put((conn, response))

    def send_response(self):
        while True:
            if not self.work_queue_done.empty():
                conn, response = self.work_queue_done.get()
                conn.send(str(response.data).encode('utf-8'))
                self.work_queue_done.task_done()

    def finish(self, signal_num, frame):
        print(f'Общее количество скаченных url равно {self.success_download}')
        raise SystemExit()


if __name__ == "__main__":
    mw = MasterWorker()
