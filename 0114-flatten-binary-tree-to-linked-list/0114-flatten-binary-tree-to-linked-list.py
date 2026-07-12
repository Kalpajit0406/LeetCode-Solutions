# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                prev = current.left
                while prev.right:
                    prev = prev.right
                
                # Connect the original right subtree to the right of prev
                prev.right = current.right
                
                # Move the left subtree to the right
                current.right = current.left
                current.left = None
                
            # Move to the next node on the right path
            current = current.right