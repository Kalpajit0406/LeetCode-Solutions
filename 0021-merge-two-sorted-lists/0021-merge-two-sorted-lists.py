# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the anchor
        dummy = ListNode()
        tail = dummy
        
        # Iterate while both lists have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Append the remaining nodes of whichever list is not empty
        tail.next = list1 if list1 else list2
        
        # Return the actual head of the merged list (skipping the dummy node)
        return dummy.next