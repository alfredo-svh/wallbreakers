class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        balloons = len(points)
        
        if balloons<=1:
            return balloons
    
        points.sort(key = lambda x: x[0])
        
        mx = points[0][1]
        arrows = 1
        
        for i in range(1,balloons):
            if points[i][0] >mx:
                arrows+=1
                mx = points[i][1]
                
            elif points[i][1] < mx:
                mx = points[i][1]
            
        return arrows