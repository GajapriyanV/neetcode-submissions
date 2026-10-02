class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        neighbours = defaultdict(list)

        for a, b in prerequisites:
            neighbours[b].append(a)
        
        path = set()
        res = []

        def dfs(node):
            if neighbours[node] == []:
                return True
            
            if node in path:
                return False
            
            path.add(node)

            for nei in neighbours[node]:
                if not dfs(nei):
                    return False
            
            neighbours[node] = []
            path.remove(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
            


        