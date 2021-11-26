from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def find_depth(node: TreeNode):
            if not node:
                return 0
            return max(find_depth(node.left), find_depth(node.right)) + 1

        def sum_max(node: TreeNode, depth: int = 1):
            if not node:
                return
            if depth == self.max_depth:
                print(f'{depth=}')
                self.ans += node.val
            sum_max(node.left,  depth + 1)
            sum_max(node.right, depth + 1)

        self.ans = 0
        self.max_depth = find_depth(root)
        sum_max(root, 1)
        return self.ans



def make_tree(lst: list):
    n = len(lst)
    if n == 0:
        return None

    def rec(i = 0):
        if i >= n or (not lst[i]):
            return None
        node = TreeNode(lst[i])
        node.left = rec(2 * i + 1)
        node.right = rec(2 * i + 2)
        return node
    return rec()


# Tests
cases = [
    [[1,2,3,4,5,None,6,7,None,None,None,None,8], 15],
    [[6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], 19],
]

s = Solution()
for c in cases:
    r = s.deepestLeavesSum(make_tree(c[0]))
    print(f'{r=}, expected {c[1]}')
    assert r == c[1]
