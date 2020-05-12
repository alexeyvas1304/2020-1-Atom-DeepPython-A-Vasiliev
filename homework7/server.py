import socket
from views import get_top_words
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()
server_socket.settimeout(300)

while True:
    client_socket, addr = server_socket.accept()
    while True:
        request = client_socket.recv(4096).decode()
        if not request:
            break
        response = get_top_words(json.loads(request)['data'])
        client_socket.send(str(response.data).encode('utf-8'))  # json.dumps показывает экранирующие слеши
    client_socket.close()  # зачем ?
