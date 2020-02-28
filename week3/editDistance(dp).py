class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1) == 0 or len(word2)==0:
            return len(word1) + len(word2)
        
        dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(dp)):
            dp[i][0] = i
        
        for i in range(len(dp[0])):
            dp[0][i] = i
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
        
        
        return dp[len(word1)][len(word2)]