class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        l =0; r = len(s)-1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        slist = list(s)
        
        while 1:
            while s[l] not in vowels and l<r:
                l+=1
            
            while s[r] not in vowels and l<r:
                r-=1
                
            if l<r:
                temp =slist[l]
                slist[l] = slist[r]
                slist[r] = temp
                r-=1
                l+=1
                
            else:
                return "".join(slist)