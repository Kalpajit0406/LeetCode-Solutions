from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_pts = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                # Reduce slope fraction to irreducible form
                g = math.gcd(dx, dy)
                slope = (dx // g, dy // g)
                
                # Ensure a consistent sign orientation for the slope tuple
                if slope[0] < 0 or (slope[0] == 0 and slope[1] < 0):
                    slope = (-slope[0], -slope[1])
                    
                slopes[slope] += 1
                
            if slopes:
                max_pts = max(max_pts, max(slopes.values()) + 1)
                
        return max_pts