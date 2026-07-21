class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        reqMap = collections.defaultdict(list)

        for crs, pre in prerequisites:
            reqMap[crs].append(pre)
        
        visit = set()
        path = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return True
            
            if crs in path:
                return False
            
            path.add(crs)

            for nei in reqMap[crs]:
                if not dfs(nei):
                    return False
            
            path.remove(crs)
            visit.add(crs)
            res.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        
        




