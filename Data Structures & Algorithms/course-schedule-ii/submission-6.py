class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        reqMap = defaultdict(list)
        res = []
        for crs, prereq in prerequisites:
            reqMap[crs].append(prereq)
        

        visit = set()
        seen = set()
        def dfs(node):
            if node in visit:
                return True
            
            if node in seen:
                return False
            
            seen.add(node)
            
            for nei in reqMap[node]:
                if not dfs(nei):
                    return False
            
            seen.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res


        