# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(node: TreeNode, level: int, gp: dict = None):
            if not node:
                return
            if not gp:
                gp = {}
            gp[level] = True if node.val % 2 == 0 else False
            if level > 2 and gp[level-2]:
                self.res += node.val
            traverse(node.left, level + 1, gp)
            traverse(node.right, level + 1, gp)
        traverse(root, 1)
        return self.res

s = Solution()
print(s.sumEvenGrandparent(TreeNode(1)))
