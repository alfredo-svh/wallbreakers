class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tempStack = []
        
        while(len(self.queue)!=1):
            tempStack.append(self.queue.pop())
        res = self.queue.pop()
        
        while(len(tempStack)!=0):
            self.queue.append(tempStack.pop())
        
        return res
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        tempStack = []
        
        while(len(self.queue)!=1):
            tempStack.append(self.queue.pop())
        res = self.queue[-1]
        
        
        while(len(tempStack)!=0):
            self.queue.append(tempStack.pop())
        
        return res
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue)==0