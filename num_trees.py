class Solution:
    def numTrees(self, n: int) -> int:
        class Node:
            def __init__(self, item):
                val = 0
                left = None
                right = None

        def make_trees(node, lst):





s = Solution()
assert s.numTrees(1) == 1
assert s.numTrees(3) == 5
