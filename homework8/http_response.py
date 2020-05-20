
class HttpResponse:
    def __init__(self, status_code=200, type_data='str', data=None):
        self.status_code = status_code
        self.type_data = type_data
        self.data = data  # подразумеваем, что json
