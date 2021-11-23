from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(n: TreeNode, res: int):
            if not n:
                return res
            return max(traverse(n.left, res + 1), traverse(n.right, res + 1))
        return traverse(root, 0)


# Test code:
s = Solution()
r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
r2 = TreeNode(1, None, TreeNode(2))
r3 = None
r4 = TreeNode(0)


assert s.maxDepth(r1) == 3
assert s.maxDepth(r2) == 2
assert s.maxDepth(r3) == 0
assert s.maxDepth(r4) == 1
