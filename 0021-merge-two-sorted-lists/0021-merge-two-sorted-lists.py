# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        if list1.val <= list2.val:
            mhead = list1
            node1 = list1.next
            node2 = list2
        else:
            mhead = list2
            node1 = list1
            node2 = list2.next
        mnode = mhead
        while node1 or node2:
            if node1 and node2:
                if node1.val <= node2.val:
                    mnode.next = node1
                    node1 = node1.next
                    mnode = mnode.next
                else:
                    mnode.next = node2
                    node2 = node2.next
                    mnode = mnode.next
            elif not node1:
                mnode.next = node2
                node2 = node2.next
                mnode = mnode.next
            else:
                mnode.next = node1
                node1 = node1.next
                mnode = mnode.next
        return mhead
