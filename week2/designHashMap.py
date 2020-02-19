class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = [False]*1000000
        self.values = [-1]*1000000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.keys[key] = True
        self.values[key] = value
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.keys[key]:
            return self.values[key]
        else:
            return -1
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.keys[key] = False