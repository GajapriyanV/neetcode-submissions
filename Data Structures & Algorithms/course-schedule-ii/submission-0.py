from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)

        for pre, req in prerequisites:
            prereq[pre].append(req)
        
        output = []
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            
            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
            

        