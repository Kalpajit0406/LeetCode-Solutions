class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down_one = 0
        down_two = 0
        
        for i in range(len(cost)):
            current = cost[i] + min(down_one, down_two)
            down_two = down_one
            down_one = current
            
        return min(down_one, down_two)