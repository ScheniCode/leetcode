"""
72. 编辑距离
https://leetcode.cn/problems/edit-distance/?envType=study-plan-v2&envId=top-100-liked

动态规划
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for index in range(m + 1):
            dp[index][0] = index
        for index in range(n + 1):
            dp[0][index] = index
        for i, a in enumerate(word1):
            for j, b in enumerate(word2):
                if a == b:
                    dp[i + 1][j + 1] = min(dp[i][j + 1]+1, dp[i + 1][j]+1, dp[i][j])
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1]+1, dp[i + 1][j]+1, dp[i][j] + 1)
        return dp[m][n]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
