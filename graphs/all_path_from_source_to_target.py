from typing import List


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dag = {}
        for i, e in enumerate(graph):
            dag[i] = e

        def find_paths(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            if start not in graph:
                return []
            paths = []
            for node in graph[start]:
                if node not in path:
                    newpaths = find_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths

        return find_paths(dag, 0, len(graph) - 1)




s = Solution()
cases = [
    [
        [[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]
    ],
    # [
    #     [[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    # ],
    # [
    #     [[1], []], [[0, 1]]
    # ],
    # [
    #     [[1, 2, 3], [2], [3], []], [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
    # ],
    # [
    #     [[1, 3], [2], [3], []], [[0, 1, 2, 3], [0, 3]]
    # ]
]

for c in cases:
    r = s.allPathsSourceTarget(c[0])
    print(r)
    assert r == c[1]
