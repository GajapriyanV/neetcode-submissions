"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        deepCopy = {}

        def dfs(node):
            if node.val in deepCopy:
                return deepCopy[node.val]

            copy = Node(node.val)
            deepCopy[node.val] = copy
            
            for nei in node.neighbors:
                copy.neighbours.append(dfs(nei))
            
            return deepCopy[node.val]
        
        return dfs(node) if node else None

        