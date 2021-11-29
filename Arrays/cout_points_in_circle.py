from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_in_circle(x, y, xr, yr, r):
            return (x-xr)**2 + (y-yr)**2 <=r**2
        ans = []
        for q in queries:
            q_ans = 0
            for p in points:
                if is_in_circle(*p, *q):
                    q_ans += 1
            ans.append(q_ans)
        return ans


        pass



cases = [
    [
        [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]], [3, 2, 2]
    ],
    [
        [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]], [2, 3, 2, 4]
    ]
]

s = Solution()
for case in cases:
    r = s.countPoints(case[0], case[1])
    print(r)
    assert r == case[2]
