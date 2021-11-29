from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
                self.memo[n] = ans

        return self.memo[n]


cases = [
    [
        7, [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]

    ],
    [
        3, [[0,0,0]]
    ],
]
s = Solution()
for c in cases:
    r = s.allPossibleFBT(c[0])
    print(r)
