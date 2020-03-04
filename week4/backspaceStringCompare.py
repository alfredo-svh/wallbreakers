class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stack1 = []
        
        stack2 = []
        
        for i in range(len(S)):
            if S[i]!= "#":
                stack1.append(S[i])
            else:
                if len(stack1)>0:
                    stack1.pop()
        
        
        for i in range(len(T)):
            if T[i]!= "#":
                stack2.append(T[i])
            else:
                if len(stack2)>0:
                    stack2.pop()
        
        return stack1==stack2