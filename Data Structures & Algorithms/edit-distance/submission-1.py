class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if n > m:
            n, m = m, n
            word1, word2 = word2, word1
        dp = [n - j for j in range(n + 1)]
        for i in range(n + 1):
            dp[i] = n - i
        for i in range(m - 1, -1, -1):
            nextDp = dp[n]
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextDp
                else:
                    dp[j] = 1 + min(temp, nextDp, dp[j + 1])
                nextDp = temp
        return dp[0]
