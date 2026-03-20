from typing import List

"""
64. 最小路径和
https://leetcode.cn/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-100-liked

动态规划 + 贪心
"""

# todo 改写为位置依赖

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for index in range(1, m):
            dp[index][0] = grid[index][0] + dp[index - 1][0]
        for index in range(1, n):
            dp[0][index] = grid[0][index] + dp[0][index - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))
