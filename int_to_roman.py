class Solution:
    digits = {
        1: 'I',
        2: 'X',
        3: 'C',
        4: 'M'
    }
    halves = {
        1: 'V',
        2: 'L',
        3: 'D'
    }

    def intToRoman(self, num: int) -> str:
        result = []
        i = 1
        remainder = num
        while True:
            d = remainder % 10
            result.append(self.convert(d, i))
            remainder = remainder // 10
            if remainder == 0:
                break
            i += 1

        result.reverse()
        return ''.join(result)


    def convert(self, d, i):
        if d == 4:
            return self.digits[i] + self.halves[i]
        elif 4 < d < 9:
            return self.halves[i] + ''.join([self.digits[i] for n in range(d-5)])
        elif d == 9:
            return self.digits[i] + self.digits[i + 1]
        else:
            return ''.join([self.digits[i] for n in range(d)])



s = Solution()

assert s.intToRoman(3) == 'III'
assert s.intToRoman(6) == 'VI'
assert s.intToRoman(4) == 'IV'
assert s.intToRoman(9) == 'IX'
assert s.intToRoman(12) == 'XII'
assert s.intToRoman(27) == 'XXVII'
assert s.intToRoman(58) == 'LVIII'
assert s.intToRoman(59) == 'LIX'
assert s.intToRoman(123) == 'CXXIII'
assert s.intToRoman(499) == 'CDXCIX'
assert s.intToRoman(1994) == 'MCMXCIV'
