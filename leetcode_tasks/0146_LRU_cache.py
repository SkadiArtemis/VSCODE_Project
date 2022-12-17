class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.double_link = DoubleLink()
        self.cap = capacity

    def makeRecently(self, key):
        x = self.hash_map[key]
        self.double_link.remove_at(x)
        self.double_link.add_last(x)

    def addRecently(self, key, value):
        x = Node(key, value)
        self.double_link.add_last(x)
        self.hash_map[key] = x
        if self.double_link.size > self.cap:
            self.removeLeastRecently()

    def deleteKey(self, key):
        x = self.hash_map[key]
        self.double_link.remove_at(x)
        del self.hash_map[key]

    def removeLeastRecently(self):
        node = self.double_link.remove_first()
        del self.hash_map[node.key]

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.makeRecently(key)
            return self.hash_map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].value = value
            self.makeRecently(key)
        else:
            self.addRecently(key, value)


class DoubleLink:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_last(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove_at(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def remove_first(self):
        if self.head.next == self.tail:
            return None
        x = self.head.next
        self.remove_at(x)
        return x


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev, self.next = None, None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)