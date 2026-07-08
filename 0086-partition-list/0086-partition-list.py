# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads for the two independent lists
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to traverse and append to the two lists
        less = less_head
        greater = greater_head
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
            
        # Crucial: Cut off any remaining chain to prevent a cycle
        greater.next = None
        
        # Connect the end of the 'less' list to the start of the 'greater' list
        less.next = greater_head.next
        
        return less_head.next