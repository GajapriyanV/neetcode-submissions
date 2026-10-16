class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        nodeMap = defaultdict(list)

        for e1, e2 in edges:
            nodeMap[e1].append(e2)
            nodeMap[e2].append(e1)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in nodeMap[node]:
                if nei == prev:
                    continue
                
                if not dfs(nei, node):
                    return False
        
            return True
        
        return dfs(0, -1)

        