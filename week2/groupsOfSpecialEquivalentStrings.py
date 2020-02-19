class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = set()
        
        for i in A:
            t = ''.join(sorted(i[0::2])) #sorted letters in even indices
            t+= ''.join(sorted(i[1::2])) #append sorted letters in odd indices
            
            #since the lenght of each word in A is the same, it works
            s.add(t)
            
        return len(s)