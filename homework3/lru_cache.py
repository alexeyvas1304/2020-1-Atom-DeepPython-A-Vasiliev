from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get_(self, key: str) -> str:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return ''

    def set_(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)  # ???
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

    def delete_(self, key: str) -> None:
        self.cache.pop(key, default=None)
