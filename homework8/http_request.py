import json


class HttpRequest:
    def __init__(self, host, port, method, data=None):
        self.host = host
        self.port = port
        self.method = method
        self.data = data  # хотя бы это
        self.request_dict = {'host': host, "port": port, "method": method, "data": data}
        self.request = json.dumps(self.request_dict, ensure_ascii=False)
