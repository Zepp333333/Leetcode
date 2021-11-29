from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        res = []
        last_partition = -1
        candidate_partition = 0
        for i in range(len(s)):
            current_char = s[i]
            if last[current_char] > candidate_partition:
                candidate_partition = last[current_char]
            if i == candidate_partition:
                res.append(i - last_partition )
                last_partition = i
        return res




s = Solution()

cases = [
    [
        "ababcbacadefegdehijhklij", [9, 7, 8]
    ],
    [
        "eccbbbbdec", [10]
    ],
]

for c in cases:
    r = s.partitionLabels(c[0])
    print(r)
    assert r == c[1]
