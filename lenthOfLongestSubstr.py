class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        results = []
        cur_result = 0
        hash = {}
        i = 0
        while True:
            if i == len(s):
                break
            char = s[i]
            if char not in hash:
                hash[char] = i
                cur_result += 1
                i += 1
            else:
                results.append(cur_result)
                i = hash[char] + 1
                hash = {}
                cur_result = 0
        results.append(cur_result)

        return sorted(results)[-1]




soluiton = Solution()
r1 = soluiton.lengthOfLongestSubstring("abcabcbb")
r2 = soluiton.lengthOfLongestSubstring("bbbbb")
r3 = soluiton.lengthOfLongestSubstring("pwwkew")
r4 = soluiton.lengthOfLongestSubstring(" ")


assert r4 == 3
assert r1 == 3
assert r2 == 1
assert r3 == 3
