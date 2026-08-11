class MyHashSet:

    def __init__(self):
        self.size = 800
        self.lis = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        val = key
        key = key % self.size
        for n in self.lis[key]:
            if n == val:
                return None
        self.lis[key].append(val)

    def remove(self, key: int) -> None:
        val = key
        key = key % self.size
        for i, n in enumerate(self.lis[key]):
            if n == val:
                self.lis[key].pop(i)

    def contains(self, key: int) -> bool:
        val = key
        key = key % self.size
        for n in self.lis[key]:
            if n == val:
                return True

        return False
