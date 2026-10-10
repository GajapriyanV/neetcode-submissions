class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = [[] for _ in range(numCourses)]
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        res= []
        
        for pre, cr in prerequisites:
            adj[cr].append(pre)
            isPrereq[cr][pre] = True
        

        def dfs(prereq, crs):

            if isPrereq[crs][prereq] != -1:
                return isPrereq[crs][prereq] == 1
            
            for nei in adj[crs]:
                if dfs(prereq, nei):
                    isPrereq[crs][prereq] = True
                    return True
            
            isPrereq[crs][prereq] = 0
            return False
        
        for pre, crs in queries:
            res.append(dfs(pre, crs))
        
        return res

        


        