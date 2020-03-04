class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c=="(":
                stack.append(c)
            elif c=="{":
                stack.append(c)
            elif c== "[":
                stack.append(c)
            elif c==")":
                if not stack or stack.pop() != "(":
                    return False
            elif c=="}":
                if not stack or stack.pop() != "{":
                    return False
            elif c=="]":
                if not stack or stack.pop() != "[":
                    return False
        
        if len(stack) >0:
            return False
        return True