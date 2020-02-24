class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mp = {}
        for i in range(len(S)):
            if S[i] not in mp:
                mp[S[i]] = [i,i]
            else:
                mp[S[i]][1] = i
        
        lst = []
        for c in mp:
            lst.append(mp[c])
            

        res = []
        l = lst[0][0]
        r = lst[0][1]
        i=1
        
        while True:
            while(i< len(lst) and lst[i][0]<= r):
                r = max(lst[i][1], r)
                i+=1
                
            res.append(r-l+1)
            
            if not i<len(lst):
                return res
            
            l = lst[i][0]
            r = lst[i][1]