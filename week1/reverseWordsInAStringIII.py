class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        s = ""
        
        for i in range(len(words)):
            s = s + words[i][::-1]
            if i < len(words) -1:
                s+=" "

        return s