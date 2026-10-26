class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges)) + 1

        def find(x):

            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(u1, u2):
            p1, p2 = find(u1), find(u2)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


        