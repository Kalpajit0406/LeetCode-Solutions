# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sentinel node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        
        # prev tracks the last node before the sublist of duplicates
        prev = dummy
        curr = head
        
        while curr:
            # If it's a start of a duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # Move curr until the end of the duplicate sequence
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip all duplicates by linking prev to curr's next node
                prev.next = curr.next
            else:
                # No duplicate detected, safely move prev forward
                prev = prev.next
                
            # Move curr forward
            curr = curr.next
            
        return dummy.next