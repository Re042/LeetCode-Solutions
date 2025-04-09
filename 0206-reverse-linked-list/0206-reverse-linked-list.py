# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        node = head
        while node.next:
            tmp = node
            node = node.next
            tmp.next = prev
            prev = tmp
        node.next = prev
        return node
            
        