# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and find the tail
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        # 2. Normalize k
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to form a circular list
        last_node.next = head
        
        # 4. Find the new tail: (length - k) steps from the head
        # We start at head, so we need to move (length - k - 1) steps
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head