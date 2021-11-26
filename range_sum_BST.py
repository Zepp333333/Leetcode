from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(node):
            if not node:
                return 0
            if node.val > high:
                return traverse(node.left)
            if node.val < low:
                return traverse(node.right)
            return node.val + traverse(node.left) + traverse(node.right)

        return traverse(root)
