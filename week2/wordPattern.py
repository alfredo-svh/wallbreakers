class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        l1 = list(pattern)
        l2 = str.split()
        
        m1 = {}
        m2 ={}
        
        if len(l1) != len(l2):
            return False
        
        for i in range(len(l1)):
            #if pattern[i] != what it's supposed to be, return false
            if l1[i] in m1:
                if m1[l1[i]] != l2[i]:
                    return False
            #if the string[i] is not what it's supposed to be, return false
            if l2[i] in m2:
                if m2[l2[i]] != l1[i]:
                    return False
            
            else:
                m1[l1[i]] = l2[i]
                m2[l2[i]] = l1[i]
        
        return True