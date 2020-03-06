class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, target, curList, res, candidates):
            if target<=0:
                if target==0:
                    res.append(curList.copy())
                return
            
            for j in range(i, len(candidates)):
                curList.append(candidates[j])
                helper(j, target-candidates[j], curList, res, candidates)
                curList.pop()
                
                
        res = []
        helper(0, target, [], res, candidates)
        
        return res