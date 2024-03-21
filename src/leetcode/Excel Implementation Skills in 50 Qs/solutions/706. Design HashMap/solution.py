class MyHashMap:

    def __init__(self):
        self.capacity = 1000000
        self.hash_map = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity  

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        self.hash_map[hash_key] = value
        

    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        if self.hash_map[hash_key] is not None:
            return self.hash_map[hash_key]
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if self.hash_map[hash_key] is not None:
            self.hash_map[hash_key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
