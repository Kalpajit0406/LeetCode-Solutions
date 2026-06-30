# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the predecessor of the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Ensure there are at least two nodes left to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping pointers
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev two nodes ahead for the next pair
            prev = first
            
        return dummy.next