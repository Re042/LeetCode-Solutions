# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        mhead = ListNode()
        prev = None
        mnode = mhead
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                prev = mnode
                mnode = node1
                prev.next = mnode
                node1 = node1.next
            else:
                prev = mnode
                mnode = node2
                prev.next = mnode
                node2 = node2.next
        while node1:
            prev = mnode
            mnode = node1
            prev.next = mnode
            node1 = node1.next
        while node2:
            prev = mnode
            mnode = node2
            prev.next = mnode
            node2 = node2.next
        return mhead.next
