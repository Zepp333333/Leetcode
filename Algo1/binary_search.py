from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            v = nums[mid]
            if target == v:
                return mid
            if target > v:
                left += 1
            if target < v:
                right -= 1
        return -1





s = Solution()
assert s.search([5], 5) == 0
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 2) == -1
assert s.search([], 9) == -1
