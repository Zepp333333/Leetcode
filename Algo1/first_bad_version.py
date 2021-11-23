# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version):
    return True if version >= 1 else False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            ptr = left + (right - left) / 2
            if isBadVersion(ptr):
                right = ptr
            else:
                left = ptr + 1
        return left
s = Solution()
assert s.firstBadVersion(4) == 1
