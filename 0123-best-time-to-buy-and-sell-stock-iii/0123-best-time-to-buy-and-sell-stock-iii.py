class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # Initialize the states for up to two transactions
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        
        for price in prices:
            # First transaction: maximize profit by minimizing effective buy price
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            # Second transaction: reinvest profit from the first transaction
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            
        return profit2