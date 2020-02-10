class Solution:
    def findComplement(self, num: int) -> int:

		#more efficient:

        h = 1
        while h <= num:
            h*=2
        return num ^ (h - 1)
        
        
'''
        #manually changing each bit using the binary representation of num as a list:
        
        s = list(bin(num)[2:])
            
        for i in range(len(s)):
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i]="1"
                
        return int("".join(s), 2)
'''