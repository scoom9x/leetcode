class MyHashSet:

    def __init__(self):
        self.lis = []

    def add(self, key: int) -> None:
        for n in self.lis:
            if n == key:
                return None

        self.lis.append(key)

    def remove(self, key: int) -> None:
        for i, n in enumerate(self.lis):
            if n == key:
                self.lis.pop(i)

    def contains(self, key: int) -> bool:
        for n in self.lis:
            if n == key:
                return True

        return False

    def __repr__(self):
        return str(self.lis)


hs = MyHashSet()

hs.add(5)

print(hs)
