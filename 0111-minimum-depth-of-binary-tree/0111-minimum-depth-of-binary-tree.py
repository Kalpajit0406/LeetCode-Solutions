# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If one of the subtrees is empty, we must take the path through the non-empty subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
            
        # If both subtrees exist, take the minimum of both paths
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1