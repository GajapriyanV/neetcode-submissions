class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for col in range(len(dp[0])):
            dp[0][col] = col

        for row in range(len(dp)):
            dp[row][0] = row

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j - 1]  # Replace
                    )

        return dp[len(word1)][len(word2)]