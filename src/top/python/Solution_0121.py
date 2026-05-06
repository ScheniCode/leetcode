"""
121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked

dp  先得到每天的利润数组   然后动态规划找到和最大的连续子数组的和
"""
from typing import List


# TODO 细节没到位   不是最优解

class Solution:
    # 只有一次交易机会
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = []
        for i in range(1, len(prices)):
            profit.append(prices[i] - prices[i - 1])
        dp = [profit[0]]
        max_p = max(0,dp[0])
        for i in range(1, len(profit)):
            p = max(profit[i],profit[i]+dp[i-1])
            dp.append(p)
            max_p = max(p,max_p)
        return max_p


if __name__ == '__main__':
    prices = [1,2]
    print(Solution().maxProfit(prices))