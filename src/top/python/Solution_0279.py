"""
279. 完全平方数
https://leetcode.cn/problems/perfect-squares/?envType=study-plan-v2&envId=top-100-liked

动态规划  背包？
        额  想多了   不是背包   就是动态规划
"""
import sys
from math import inf, sqrt, ceil


class Solution:
    # TODO 麻了  dp定义好想  状态转移公式...    下次看下数学方法

    def numSquares(self, n: int) -> int:
        dp = [0,1]
        for i in range(2,n+1):
            min_num = sys.maxsize
            j = 1
            while j*j <= i:
                min_num = min(min_num,dp[i - j*j])
                j+=1
            dp.append(int(min_num) + 1)
        return dp[n]

if __name__ == '__main__':
    Solution().numSquares(12)