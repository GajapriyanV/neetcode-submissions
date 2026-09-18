class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        for edge, val in zip(equations, values):
            e1, e2 = edge

            graph[e1].append((e2, val))
            graph[e2].append((e1, 1 / val))

        final_res = []

        def bfs(start, end):

            # Variable doesn't exist
            if start not in graph or end not in graph:
                return -1.0

            q = deque([(start, 1.0)])
            visit = {start}

            while q:
                cur, ans = q.popleft()

                if cur == end:
                    return ans

                for nei, val in graph[cur]:

                    if nei not in visit:
                        visit.add(nei)
                        new_ans = ans * val
                        q.append((nei, new_ans))

            return -1.0

        for start, end in queries:
            final_res.append(bfs(start, end))

        return final_res