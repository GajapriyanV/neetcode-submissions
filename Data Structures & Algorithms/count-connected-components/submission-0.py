class UnionFind:
    def __init__(self, n) -> None:
        
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
            self.parent[x] = self.parent[self.parent[x]]
        
        return x
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] += p2
            self.rank[p2] = self.rank[p1]
        return 1

    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for e1, e2 in edges:
            n -= uf.union(e1, e2)
        
        return n

        