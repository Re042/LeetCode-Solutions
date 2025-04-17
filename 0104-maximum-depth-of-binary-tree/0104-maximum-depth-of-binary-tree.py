# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], k = 0) -> int:
        if not root:
            return k
        k += 1
        A = self.maxDepth(root = root.right, k = k)
        B = self.maxDepth(root = root.left,  k = k)
        return A if A>=B else B