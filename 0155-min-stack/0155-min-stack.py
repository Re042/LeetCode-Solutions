class Node:
    def __init__(self, val = None, mel = None):
        self.val = val
        self.mel = mel
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val = val, mel = val)
            return
        if self.head.mel > val:
            mel = val
        else:
            mel = self.head.mel
        node = Node(val = val, mel = mel)
        node.next = self.head
        self.head = node
        return

    def pop(self) -> None:
        self.head = self.head.next
        return

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.mel


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()