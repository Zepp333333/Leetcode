class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = abs(x)
        result = 0
        for i in range(0, len(str(num))):
            digit = num % 10
            result = (result * 10) + digit
            num = (num - digit) // 10
        result *= sign
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return result




sol = Solution()
assert sol.reverse(123) == 321
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(0) == 0
assert sol.reverse(1999999999) == 0
assert sol.reverse(-1999999999) == 0
assert sol.reverse(5463847412) == 2147483645
assert sol.reverse(8463847412) == 0
assert sol.reverse(-8463847412) == -2147483648
