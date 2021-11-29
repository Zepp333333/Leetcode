from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for e in nums:
                ans.append(e)
        return ans

s = Solution()
t = [
    [[1,2,1], [1,2,1,1,2,1]],
    [[1,3,2,1], [1,3,2,1,1,3,2,1]],

    ]

for c in t:
    a = s.getConcatenation(c[0])
    print(a)
    assert a == c[1]
