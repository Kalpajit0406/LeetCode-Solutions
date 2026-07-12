# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
                
            # Max sum on the left and right subtrees (ignore negative gains)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price of the path starting at the current node and using both children
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            max_sum = max(max_sum, current_path_sum)
            
            # For the parent call, return the maximum gain the node can contribute
            return node.val + max(left_gain, right_gain)
            
        max_gain(root)
        return max_sum