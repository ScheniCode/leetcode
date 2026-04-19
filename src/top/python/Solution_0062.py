"""
62. 不同路径
https://leetcode.cn/problems/unique-paths/?envType=study-plan-v2&envId=top-100-liked

总步数是m+n-2    排列组合$(C_m+n-2)^m-1$
"""

dp = [0, 1]


def step(n: int) -> int:
    if len(dp) >= n + 1:
        return dp[n]
    else:
        pre = step(n - 1)
        dp.append(pre * n)
    return dp[n]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return step(m-1 + n-1) // step(n-1) // step(m-1)


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
