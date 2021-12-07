class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == ''.join(list(reversed(s)))

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        right = 0
        while right < x:
            right = right * 10 + x % 10
            x = x // 10
        return x == right or x == right // 10






# constraints: -231 <= x <= 231 - 1
# test code
s = Solution()
tests = [
    [121, True],
    [0, True],
    [-121, False],
    [10, False],
    [-101, False],
    [11, True]
]
for test in tests:
    r = s.isPalindrome2(test[0])
    print(r)
    assert r == test[1]
