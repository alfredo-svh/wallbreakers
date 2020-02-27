class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(s,p, i,j,mem):
            #base case
            if j==len(p):
                if i ==len(s):
                    return True
                else:
                    return False
            
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            
            #case i+1 == *
            if j<len(p)-1 and p[j+1]=="*":
                if i==len(s):
                    if j+2 == len(p):
                        mem[(i,j)] = True
                    else:
                        mem[(i,j)] = helper(s,p,i,j+2, mem)
                
                #case matching 1
                elif i<len(s) and s[i] == p[j] or p[j]==".":
                    mem[(i,j)] =  helper(s,p,i+1,j, mem) or helper(s,p,i,j+2, mem)
                
                #case 0
                else:
                    mem[(i,j)] = helper(s,p,i,j+2, mem)
            
            elif i==len(s):
                mem[(i,j)] =  False
            
            #case matching
            elif s[i] == p[j] or p[j]==".":
                mem[(i,j)] =  helper(s,p,i+1,j+1, mem)
            
            else:
                mem[(i,j)] =  False
            
            return mem[(i,j)]
            
            
        mem = {}
        
        return helper(s,p,0,0,mem)