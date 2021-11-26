from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def build(preorder, parent):
            print(preorder)
            if not preorder:
                return None
            if preorder[0] == parent:
                return None
            node = TreeNode(preorder[0])
            parent = node.val
            split = self.find_split(preorder[1:], preorder[0])
            node.left = build(preorder[1:][:split], parent)
            if split:
                node.right = build(preorder[1:][split:], parent)

            return node

        return build(preorder, None)

    def find_split(self, lst: list, n: int):
        for i, e in enumerate(lst):
            if e > n:
                return i

s = Solution()
r = s.bstFromPreorder([4,2,2])
r2 = s.bstFromPreorder([1,3])
