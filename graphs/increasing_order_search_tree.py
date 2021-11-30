# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def traverse(node: TreeNode, lst=None):
            if lst is None:
                lst = []
            if not node:
                return
            lst.append(node.val)
            traverse(node.left, lst)
            traverse(node.right, lst)
            return lst

        def make_tree(v: list):
                return TreeNode(v[0], None, make_tree(v[1:])) if v else None

        return make_tree(sorted(traverse(root)))

s = Solution()
r = s.increasingBST(TreeNode(5, TreeNode(1), TreeNode(7)))
print(r)
assert r == TreeNode(1, None, TreeNode(5, None, TreeNode(7)))
