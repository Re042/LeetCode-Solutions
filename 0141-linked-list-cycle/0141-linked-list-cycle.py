# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        left = head
        right = head.next.next
        if not right:
            return False
        while left != right:
            left = left.next
            for _ in range(2):
                if not right.next:
                    return False
                right = right.next
        return True