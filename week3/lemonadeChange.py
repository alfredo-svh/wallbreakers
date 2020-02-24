class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0,20:0}
        
        for bill in bills:
            #$10
            if bill ==10:
                if change[5]<1:
                    return False
                change[5]-=1
            
            #$20
            elif bill == 20:
				#we have a $10
                if change[10]>=1:
                    if change[5]>=1:
                        change[10]-=1
                        change[5]-=1
                    else:
                        return False
						
				#we don't have a $10
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
                
            change[bill]+=1
        
        return True