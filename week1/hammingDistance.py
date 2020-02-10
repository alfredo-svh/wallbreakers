class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

		#using xor:
		dist = 0
		h = bin(x^y)

		for i in h:
			if i == '1':
				dist+=1

		return dist



'''
		#manually counting:

        dist = 0
        s1 = '{:032b}'.format(x)
        s2 = '{:032b}'.format(y)
        
        for i in range(32):
            if s1[i]!= s2[i]:
                dist+=1
                
        return dist
'''