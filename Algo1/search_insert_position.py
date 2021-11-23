"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
        return left




s = Solution()

n = [
    [[1,3,5,6], 5, 2],
    [[1,3,5,6], 2, 1],
    [[1,3,5,6], 7, 4],
    [[1,3,5,6], 0, 0],
    [[1], 0, 0],
]

for c in n:
    r = s.searchInsert(c[0], c[1])
    print(f'{r=}, expected = {c[2]}')
    assert s.searchInsert(c[0], c[1]) == c[2]
