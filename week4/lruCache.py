class Node:
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.len = 0
        self.head = Node(None, None)
        self.last = Node(None, None)
        self.head.next = self.last
        self.last.prev = self.head
        self.map = {}
        

    def get(self, key: int) -> int:
        if key in self.map:
            if self.map[key].next != self.last:
                self.map[key].prev.next = self.map[key].next
                self.map[key].next.prev = self.map[key].prev
                
                self.last.prev.next = self.map[key]
                self.map[key].prev = self.last.prev
                self.map[key].next = self.last
                self.last.prev = self.map[key]
            return self.map[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.len==self.maxSize and key not in self.map:
            #delete lru
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            del self.map[temp.key]
            del temp
            #insert new
            nw = Node(key, value)
            nw.next = self.last
            nw.prev = self.last.prev
            self.last.prev.next = nw
            self.last.prev = nw
            self.map[key] = nw
            
            return
        
        if key in self.map:
            #update node
            self.map[key].val = value
            #bring to last
            if self.map[key].next != self.last:
                self.map[key].prev.next = self.map[key].next
                self.map[key].next.prev = self.map[key].prev
                self.last.prev.next = self.map[key]
                self.map[key].prev = self.last.prev
                self.map[key].next = self.last
                self.last.prev = self.map[key]
            
        else:
            #insert to map, ll
            nw = Node(key, value)
            nw.next = self.last
            nw.prev = self.last.prev
            self.last.prev.next = nw
            self.last.prev = nw
            self.map[key] = nw
            
            self.len+=1