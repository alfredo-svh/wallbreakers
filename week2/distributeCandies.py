class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        s = set(candies)
        
        return int(min(len(s), len(candies)/2))