class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        neighbours = defaultdict(list)

        for a, b in prerequisites:
            neighbours[b].append(a)

        path = set()
        visited = set()
        res = []

        def dfs(node):
            # Already fully processed
            if node in visited:
                return True

            # Cycle detected
            if node in path:
                return False

            path.add(node)

            for nei in neighbours[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            visited.add(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res[::-1]