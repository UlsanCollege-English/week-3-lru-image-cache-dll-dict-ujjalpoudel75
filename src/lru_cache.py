
### `/src/lru_cache.py` (starter)
    
class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        assert capacity > 0
        self.cap = capacity
        self.map = {}
        # sentinels
        self.head = _Node("__H__", None)  # most recent after head
        self.tail = _Node("__T__", None)  # least recent before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        ...

    def put(self, key, val):
        ...
