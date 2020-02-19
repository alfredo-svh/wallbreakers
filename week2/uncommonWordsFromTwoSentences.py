class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        #split strings into lists
        l1 = A.split()
        l2 = B.split()
        
        pos = set()
        impos = set()
        
        #if word is seen more than one, it goes to impos,
        #else, it goes to pos
        for i in l1:
            if i in pos:
                pos.remove(i)
                impos.add(i)
            elif i not in impos:
                pos.add(i)
                
        #if word is not in either set, add to pos
        #if it is in pos, remove it and add it to impos
        for i in l2:
            if i in impos:
                continue
                
            if i in pos:
                pos.remove(i)
                impos.add(i)
            
            else:
                pos.add(i)
                
            
        return list(pos)