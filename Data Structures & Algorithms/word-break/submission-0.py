class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                j = len(w)
                if i + j < len(s) and s[i: i + j] == w:
                    dp[i] = dp[i + j]
                if dp[i]:
                    break
        
        return dp[0]


        