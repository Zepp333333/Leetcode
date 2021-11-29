class Solution:
    memo = {}
    def countVowelStrings(self, n: int) -> int:

        def rec(n, k):
            if k == 1 or n == 1:
                return k
            if (n, k) in self.memo:
                return self.memo[n,k]
            self.memo[n,k] = sum(rec(n-1, k) for k in range(1, k + 1))
            return self.memo[n,k]
        return rec(n, 5)




s = Solution()
print(s.countVowelStrings(2))
# assert s.countVowelStrings(1) == 5
# assert s.countVowelStrings(2) == 15
# assert s.countVowelStrings(33) == 66045
