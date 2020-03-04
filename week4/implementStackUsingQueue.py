class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tempQ = []
        
        while len(self.stack)!=1:
            tempQ.append(self.stack[0])
            del self.stack[0]
        
        res = self.stack[0]
        del self.stack[0]
        
        while len(tempQ)!=0:
            self.stack.append(tempQ[0])
            del tempQ[0]
        
        return res
        

    def top(self) -> int:
        """
        Get the top element.
        """
        tempQ = []
        
        while len(self.stack)!=0:
            res = self.stack[0]
            tempQ.append(self.stack[0])
            del self.stack[0]
        
        
        while len(tempQ)!=0:
            self.stack.append(tempQ[0])
            del tempQ[0]
        
        return res
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack)==0