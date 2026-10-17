class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edj_count = {}
        leaves = deque()

        for src, neighbors in adj.items():
            edj_count[src] = len(neighbors)
            if edj_count[src] == 1:
                leaves.append(src)
        
        while n > 2:
            for _ in range(len(leaves)):
                leaf = leaves.popleft()

                for nei in adj[leaf]:
                    edj_count[nei] -=1

                    if edj_count[nei] == 1:
                        leaves.append(nei)
                
                n-=1
        
        return list(leaves)
