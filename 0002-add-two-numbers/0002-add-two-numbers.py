# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        head = ListNode()
        node = head
        prev = None
        k = 0
        while node1 and node2:
            s = node1.val + node2.val + k
            node.val = s % 10
            k = 1 if s > 9 else 0
            node.next = ListNode()
            prev = node
            node = node.next
            node1 = node1.next
            node2 = node2.next
        while node1:
            s = node1.val + k
            node.val = s % 10
            k = 1 if s > 9 else 0
            node.next = ListNode()
            prev = node
            node = node.next
            node1 = node1.next
        while node2:
            s = node2.val + k
            node.val = s % 10
            k = 1 if s > 9 else 0
            node.next = ListNode()
            prev = node
            node = node.next
            node2 = node2.next
        if k == 1:
            node.val = 1
        else:
            prev.next = None
        return head