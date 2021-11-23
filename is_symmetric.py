from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(left: TreeNode, right: TreeNode):
            if (not left) or (not right):
                return left == right
            if left.val != right.val:
                return False
            return traverse(left.left, right.right) and traverse(left.right, right.left)
        return traverse(root.left, root.right)

# [1,2,2,null,3,null,3]
# [1,2,2,2,null,2]
s = Solution()
print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(2), None),
                             TreeNode(2, TreeNode(2)))))
