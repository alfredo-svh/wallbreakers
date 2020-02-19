class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        res = []
        ms = collections.Counter()
        
        for i in range(len(cpdomains)):
            
            tmp = cpdomains[i].split() #split number and website
            
            num = int(tmp[0])
            
            ms.update({tmp[1]: num}) #full site
            
            tmp = tmp[1].split('.') #tmp is now a list with each part of the website
            
            for j in range(1, len(tmp)):
                if j +1 == len(tmp)-1: #second-level domain
                    ms.update({tmp[j] + "."+ tmp[j+1]: num})
                else:
                    ms.update({tmp[j]: num}) #top-level domain
        
        
        #populate res
        for i in ms:
            res.append(str(ms[i]) + " "+ i)
        
        return res