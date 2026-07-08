class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores indices
        max_area = 0
        # Append 0 to flush out remaining elements in the stack at the end
        heights.append(0) 
        
        for i in range(len(heights)):
            # Maintain a monotonic increasing stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # If stack is empty, it means the popped height was the smallest so far,
                # so the width extends all the way from index 0 to i.
                w = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, h * w)
                
            stack.append(i)
            
        return max_area