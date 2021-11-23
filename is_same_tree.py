from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(p: TreeNode, q: TreeNode):
            if (not p) or (not q):
                return p == q
            if p.val != q.val:
                return False
            return traverse(p.left, q.left) and traverse(p.right, q.right)
        return traverse(p, q)


# Test code:
s = Solution()

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
assert s.isSameTree(p, q) == True

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
assert s.isSameTree(p, q) == False

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
assert s.isSameTree(p, q) == False
