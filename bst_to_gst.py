
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left:
            self.bstToGst(root.left)
        return root


class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.keys = []

        def collect_keys(node):
            if not node:
                return 0
            self.keys.append(node.val)
            collect_keys(node.left)
            collect_keys(node.right)

        def traverse(node):
            if not node:
                return
            node.val += get_sum_of_greater(node.val)
            traverse(node.left)
            traverse(node.right)

        def get_sum_of_greater(n):
            if n + 1 in self.keys:
                return sum(self.keys[self.keys.index(n + 1):])
            return sum([e for e in self.keys if e > n])

        collect_keys(root)
        self.keys.sort()
        traverse(root)
        return root
