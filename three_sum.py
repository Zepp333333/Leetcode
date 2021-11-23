from typing import List
from itertools import permutations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()
        for i in range(len(nums) -2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                summary = nums[start] + nums[i] + nums[end]
                if summary == 0:
                    candidate = [nums[start], nums[i], nums[end]]
                    if candidate not in result:
                        result.append(candidate)
                    start += 1
                    end -= 1
                elif summary < 0:
                    start += 1
                elif summary > 0:
                    end -= 1

        print(result)
        return result

    def is_inlist(self, t, lst):
        perm = list(permutations(t))
        for p in perm:
            if list(p) in lst:
                return True
        return False



s = Solution()
assert s.threeSum([]) == []
assert s.threeSum([1,2,-2,-1]) == []
assert s.threeSum([0]) == []
assert s.threeSum([0, 0, 1]) == []
assert s.threeSum([1, 1, 1]) == []
assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
