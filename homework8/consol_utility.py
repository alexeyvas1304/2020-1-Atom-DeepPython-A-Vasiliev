import argparse
import os
from collections import defaultdict
import json
import socket
from http_request import HttpRequest
import threading
from queue import Queue

parser = argparse.ArgumentParser(description='client')
parser.add_argument('path', type=str, help='path to file with urls')
parser.add_argument('threads', type=int, help='count of threads')
args = parser.parse_args()

with open(args.path, 'r') as f:
    urls = f.read().splitlines()

work_queue = Queue()
for url in urls:
    work_queue.put(url)


def worker(work_queue, i):
    while True:
        url = work_queue.get()
        print(i)
        sock = socket.socket()
        try:
            sock.connect(('localhost', 5000))
            http_request = HttpRequest(host='localhost', port=5000, method="GET", data=url)
            sock.sendall(http_request.request.encode('utf-8'))
            data = sock.recv(2 ** 12)
            sock.close()
            print(data.decode('utf-8'))
        except ConnectionRefusedError:
            print("Server doesn't work")
        work_queue.task_done()


for i in range(args.threads):
    t = threading.Thread(target=worker, args=(work_queue, i))
    t.setDaemon(True)
    t.start()
work_queue.join()
