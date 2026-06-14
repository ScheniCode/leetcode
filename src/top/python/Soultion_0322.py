"""
322. 零钱兑换
https://leetcode.cn/problems/coin-change/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def coinChange_v1(self, coins: List[int], amount: int) -> int:
        """
        由i枚硬币可以组成的金额推i+1枚可以凑出的整数，当命中amount时i就是解
        i超过amount//coins(min)+1时无解
        超时了...
        :param coins:
        :param amount:
        :return:
        """
        coins.sort()
        dp = [False] * (amount + 1)
        dp[0] = True
        i = 0
        count = amount//coins[0] + 1

        while not dp[amount] and i < count:
            pre = dp.copy()
            for index, b in enumerate(pre):
                if b:
                    for c in coins:
                        if index + c <= amount:
                            dp[index+c] = True
                        else:
                            break
            i += 1
        return i if dp[amount] else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i] i金额时的最小硬币数
        :param coins:
        :param amount:
        :return:
        """
        dp = [int(1e9)] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != int(1e9) else -1

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    sol = Solution().coinChange(coins, amount)
    print(sol)