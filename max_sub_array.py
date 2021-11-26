from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = None
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum) if ans else cur_sum
        return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            print(f'{i=}, {dp=}, {nums[i]=} ')
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)

# Tests:
n = [
    [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
    [[1], 1],
    [[5, 4, -1, 7, 8], 23],
]

s = Solution()
for test in n:
    # print(test)
    assert s.maxSubArray(test[0]) == test[1]
