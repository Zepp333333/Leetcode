from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        letter_combination = [letters[n] for n in digits]
        perm = list(product(*letter_combination))
        return [''.join(e) for e in perm]


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def rec(digits):
            if not digits:
                return []
            if len(digits) == 1:
                return [d for d in letters[digits]]
            first_digit = digits[0]
            res = []
            for first_letter in letters[first_digit]:
                for second_letter in rec(digits[1:]):
                    res.append(first_letter + second_letter)
            return res
        return rec(digits)




s = Solution2()
assert s.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert s.letterCombinations('') == []
assert s.letterCombinations('2') == ["a", "b", "c"]
