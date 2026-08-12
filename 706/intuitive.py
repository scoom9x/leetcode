class MyHashMap:

    def __init__(self):
        self.size = 729
        self.vals = [[] for _ in range(self.size)]
        self.keys = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        bucketKey = None

        for i, n in enumerate(self.keys[idx]):
            if n == key:
                bucketKey = i

        if bucketKey != None:
            self.vals[idx][bucketKey] = value
            return None

        self.keys[idx].append(key)
        self.vals[idx].append(value)

    def get(self, key: int) -> int:
        idx = key % self.size
        bucketKey = None

        for i, n in enumerate(self.keys[idx]):
            if n == key:
                bucketKey = i

        if bucketKey != None:
            return self.vals[idx][bucketKey]

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        bucketKey = None

        for i, n in enumerate(self.keys[idx]):
            if n == key:
                bucketKey = i
                self.keys[idx].pop(i)
                break

        if bucketKey != None:
            self.vals[idx].pop(bucketKey)
