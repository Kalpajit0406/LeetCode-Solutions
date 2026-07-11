# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = len(postorder) - 1
        
        def array_to_tree(left, right):
            nonlocal post_idx
            if left > right:
                return None
            
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            
            root.right = array_to_tree(inorder_map[root_val] + 1, right)
            root.left = array_to_tree(left, inorder_map[root_val] - 1)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)