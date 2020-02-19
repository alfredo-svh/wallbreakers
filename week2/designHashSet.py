class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = [False]*1000000

    def add(self, key: int) -> None:
        self.lst[key] = True

    def remove(self, key: int) -> None:
        self.lst[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return (self.lst[key])