from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def rec(nums: List[int]):
            if not nums:
                return
            root_i = max(nums)
            node = TreeNode(root_i)
            pre = nums[:nums.index(root_i)]
            post = nums[nums.index(root_i) + 1:]
            node.left = rec(pre)
            node.right = rec(post)
            return node

        return rec(nums)
