"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        biject = {}
        node = head
        while node:
            biject[node] = Node(x = node.val)
            node = node.next
        for node in biject:
            biject[node].next = biject[node.next] if node.next is not None else None
            biject[node].random = biject[node.random] if node.random is not None else None
        return biject[head]
