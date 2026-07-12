# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                # Connection 1: Children of the same parent
                head.left.next = head.right
                
                # Connection 2: Children of adjacent parents
                if head.next:
                    head.right.next = head.next.left
                    
                head = head.next
                
            leftmost = leftmost.left
            
        return root