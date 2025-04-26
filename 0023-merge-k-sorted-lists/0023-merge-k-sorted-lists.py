# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        val = []
        for head in lists:
            tmp = head
            while tmp:
                val.append(tmp.val)
                tmp = tmp.next
        val.sort()
        if not val:
            return None
        head = ListNode(val = val[0])
        node = head
        for i in range(1, len(val)):
            node.next = ListNode(val = val[i])
            node = node.next
        return head