class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        total=0
        
        for i in range(len(ops)):
            
            if ops[i]== "+":
                stack.append(stack[-2] + stack[-1])
                total+=stack[-1]
                
            elif ops[i]=="D":
                stack.append(2*stack[-1])
                total+=stack[-1]
            
            elif ops[i]=="C":
                total-= stack.pop()
            
            else:
                stack.append(int(ops[i]))
                total+=stack[-1]
        
        
        return total