from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_child(self, n: TreeNode):
        return n and (n.right or n.left)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def traverse(n: TreeNode):
            if not n:
                return True
            if not n.left and self.has_child(n.right):
                return False
            if not n.right and self.has_child(n.left):
                return False
            return traverse(n.left) and traverse(n.right)
        return traverse(root)
