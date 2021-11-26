# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None
        def traverse(o_node: TreeNode, c_node: TreeNode):
            if not o_node:
                return
            if o_node == target:
                self.res = c_node
            traverse(o_node.left, c_node.left)
            traverse(o_node.right, c_node.right)
        traverse(original, cloned)
        return self.res


s = Solution()
o = TreeNode(7, TreeNode(4, None, None), TreeNode(3, TreeNode(6), TreeNode(19)))
c = TreeNode(7, TreeNode(4, None, None), TreeNode(3, TreeNode(6), TreeNode(19)))
t = o.right
r = s.getTargetCopy(o, c, t)
print(r)
assert r == c.right
