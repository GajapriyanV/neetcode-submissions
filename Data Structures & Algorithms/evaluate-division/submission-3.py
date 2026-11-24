class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjMap = defaultdict(list)
        res = []

        for (src, dest), val in zip(equations, values):
            adjMap[src].append((dest, val))
            adjMap[dest].append((src, 1 / val))

        def bfs(src, dest):
            if src not in adjMap or dest not in adjMap:
                return -1.0

            q = deque([(src, 1.0)])
            visit = {src}

            while q:
                node, val = q.popleft()

                if node == dest:
                    return val

                for nei, neiVal in adjMap[node]:
                    if nei not in visit:
                        visit.add(nei)
                        newVal = val * neiVal
                        q.append((nei, newVal))

            return -1.0

        for src, dest in queries:
            res.append(bfs(src, dest))

        return res