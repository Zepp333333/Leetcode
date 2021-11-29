from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m+1))
        res = []
        for i in queries:
            pi = p.index(i)
            res.append(pi)
            p = [i] + p[:pi] + p[pi+1:]
        return res


cases = [
    [
        [3, 1, 2, 1], 5, [2, 1, 2, 1]
    ],
    [
        [4, 1, 2, 2], 4, [3, 1, 2, 0]
    ],
    [
        [7, 5, 5, 8, 3], 8, [6, 5, 0, 7, 5]
    ],

]

s = Solution()
for c in cases:
    r = s.processQueries(c[0], c[1])
    print(r)
    assert r == c[2]
