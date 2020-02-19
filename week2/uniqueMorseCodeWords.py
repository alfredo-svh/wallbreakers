class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        strs = set()
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        #for each word
        for word in words:
            s = ""
            
            #for each letter
            for letter in word:
                #translate, add to string
                s+=code[ord(letter) - ord('a')]
            
            #check if it's there before
            if s not in strs:
                strs.add(s)
        
        return len(strs)