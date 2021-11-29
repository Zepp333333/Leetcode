from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = {p:[] for p in range(len(groupSizes))}
        for p, group in res.items():
            if not group:
                size = groupSizes[p]
                group = [p]
                res[p] = [p]
                q = p + 1
                while len(res[p]) < size:
                    if groupSizes[q] == size:
                        res[p].append(q)
                        res[q] = res[p]
                    q += 1
        l = [r for r in res.values()]
        l.sort()
        return [l[e] for e in range(len(l)) if e == 0 or l[e] != l[e-1]]





        # p = 0
        # while p < len(groupSizes):
        #     if p == 1:
        #         res.append[p]
        #     else:
        #         gs = groupSizes[p]
        #         grp = [p]
        #         i = p+1
        #         while len(grp) < gs:
        #             print(p, i)
        #             if groupSizes[i] == gs:
        #                 grp.append(i)
        #             i += 1
        #         p = i
        #         res.append(grp)
        # return res


r1 = Solution().groupThePeople([3,3,3,3,3,1,3])
print(r1)



r2 = Solution().groupThePeople([2,1,3,3,3,2])
print(r2)
