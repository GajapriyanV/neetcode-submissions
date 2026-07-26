class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur = []

        def dfs(open, close):
            if open == 0 and close == 0:
                res.append("".join(cur))
                return
            
            
            if open > 0:
                cur.append("(")
                dfs(open - 1, close)
                cur.pop()
            
            if open < close:
                cur.append(")")
                dfs(open, close - 1)
                cur.pop()
        
        dfs(n,n)
        return res
        