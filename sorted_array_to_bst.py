from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = make_tree(l, mid-1)
            root.right = make_tree(mid+1, r)
            return root
        return make_tree(0, len(nums) - 1)



# test code
s = Solution()

i1 = [-10,-3,0,5,9]
i2 = [1,3]
r = s.sortedArrayToBST(i1)
assert s.sortedArrayToBST(i1) == TreeNode(0, TreeNode(-3, TreeNode(-10)),
                                          TreeNode(9, TreeNode(5)))
r2 = s.sortedArrayToBST(i2)
assert s.sortedArrayToBST(i2) == TreeNode(3, TreeNode(1))
