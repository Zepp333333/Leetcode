from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, _ in enumerate(nums):
            ans.append(nums[nums[i]])
        return ans

s = Solution()
n1 = [0,2,1,5,3,4]
a1 = [0,1,2,4,5,3]

n2 = [5,0,1,2,3,4]
a2 = [4,5,0,1,2,3]

r1 = s.buildArray(n1)
print(r1)
r2 = s.buildArray(n2)
print(r2)
assert r1 == a1
assert r2 == a2
