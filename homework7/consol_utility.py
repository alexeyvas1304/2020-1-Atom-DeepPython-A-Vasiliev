import socket
from http_request import HttpRequest

while True:
    url = input("Введите url страницы:\n")
    if url.strip() == 'exit()':
        break
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

