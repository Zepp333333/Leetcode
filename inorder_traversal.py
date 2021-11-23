# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec(node: TreeNode, lst: list = []):
            if node:
                rec(node.left, lst)
                lst.append(node.val)
                rec(node.right, lst)
            return lst

        return rec(root)




# def make_tree(l: lst):
#     def get_root(node, root):
#

s = Solution()

n = [TreeNode(1, None, TreeNode(2, TreeNode(3))), [1,3,2]]
n = [None,[]]
n = [TreeNode(1, None, None),[1]]
n = [TreeNode(1, TreeNode(2)), [2, 1]]
n = [TreeNode(1, None, TreeNode(2)), [1, 2]]
# n = [
#     [[1,None,2,3], [1,3,2]],
#     [[], []],
#     [[1], [1]],
#     [[1,2], [2,1]],
#     [[1,None,2], [1,2]],
# ]

r = s.inorderTraversal(n[0])
print(f'{r=}')
assert r == n[1]

# for c in n:
#     r = s.inorderTraversal(c[0])
#     print(f'{r=}, expected = {c[1]}')
#     assert r == c[1]
