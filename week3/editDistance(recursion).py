class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(word1, word2, i, j, mem):
            if i ==-1 or j ==-1:
                return max(i,j)+1

            if(i, j) not in mem:
                if word1[i] == word2[j]:
                    mem[(i,j)] = helper(word1,word2, i-1,j-1, mem)
                else:
                    mem[(i,j)] = 1 + min(helper(word1,word2, i-1,j-1, mem), helper(word1,word2, i-1,j, mem), helper(word1,word2, i,j-1, mem))
            
            
            return mem[(i,j)]
            
            
        mem = {}
        return helper(word1, word2, len(word1)-1, len(word2)-1, mem)