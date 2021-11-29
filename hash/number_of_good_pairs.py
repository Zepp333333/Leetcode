from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) -1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res

s = Solution()

cases = [
    [
        [1, 2, 3, 1, 1, 3], 4
    ],
    [
        [1, 1, 1, 1], 6
    ],
    [
        [1, 2, 3], 0
    ]
]

for c in cases:
    r = s.numIdenticalPairs(c[0])
    print(r)
    assert r == c[1]
