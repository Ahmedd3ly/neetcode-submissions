class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}

        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left       

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]        
