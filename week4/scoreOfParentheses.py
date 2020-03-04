class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        score = 0
        
        for i in range(0,len(S)):
            
            if S[i]==")":
                prev = stack.pop()
                #prev = "("
                if prev == 0:
                    to_add = 1
                #prev = ")"
                else:
                    to_add = 2*prev
                stack.append(stack.pop() + to_add)
                
            #'('
            else:
                stack.append(0)
        
        
        return stack.pop()