from typing import List

"""
322. 零钱兑换
https://leetcode.cn/problems/coin-change/description/?envType=study-plan-v2&envId=top-100-liked

动态规划   背包问题
"""

# TODO dp[i] 凑够i面额所需的最小硬币数

def f(i, sum, amount, coins):
    if i == len(coins):
        if sum == amount:
            return True
    f(i + 1, sum, amount, coins)
    while sum + coins[i] <= amount:
        r = f(i + 1, sum + coins[i], amount, coins)
        if r:
            return True
    return False


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        l = len(coins)
        for i in range(l):
            dp.append([0]* (amount + 1))
        for i in range(l):
            for j in range(1,amount + 1):
                dp[i][j] = dp[i][j-1] + coins[i]
