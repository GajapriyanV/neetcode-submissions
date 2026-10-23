
from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjMap = defaultdict(list)

        for eq, val in zip(equations, values):
            src, dest = eq
            adjMap[src].append((dest, val))
            adjMap[dest].append((src, 1 / val))

        def bfs(src, dest):
            if src not in adjMap or dest not in adjMap:
                return -1.0

            q = deque([(src, 1.0)])
            visit = set([src])

            while q:
                for _ in range(len(q)):
                    dst, val = q.popleft()

                    if dst == dest:
                        return val

                    for nei, newval in adjMap[dst]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append((nei, val * newval))

            return -1.0

        res = []
        for src, dest in queries:
            res.append(bfs(src, dest))

        return res
