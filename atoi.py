class Solution:
    def myAtoi(self, s: str) -> int:
        digits = '1234567890'
        sign = 1
        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = []
        for c in s:
            if c not in digits:
                break
            result.append(c)

        if not result:
            return 0

        integer = int(''.join(result)) * sign
        if integer > 2**31-1:
            return 2**31-1

        if integer < -2**31:
            return -2**31

        return integer








sol = Solution()
assert  sol.myAtoi("0") == 0
assert  sol.myAtoi("") == 0
assert  sol.myAtoi(" ") == 0
assert  sol.myAtoi(" -") == 0
assert  sol.myAtoi("42") == 42
assert  sol.myAtoi("-42") == -42
assert  sol.myAtoi("   -42") == -42
assert  sol.myAtoi("4193 with words") == 4193
assert  sol.myAtoi("words and 987") == 0
assert  sol.myAtoi("-91283472332") == -2147483648
