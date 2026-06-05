"""
53. 最大子数组和
https://leetcode.cn/problems/maximum-subarray/?envType=study-plan-v2&envId=top-100-liked

前缀和  or  动态规划
"""
from typing import List


class Solution:

    def maxSubArrayV1(self, nums: List[int]) -> int:
        """
        前缀和
        :param nums:
        :return:
        """
        pre = [0]
        for n in nums:
            pre.append(pre[-1]+n)
        minIndex = 0
        maxSubSum = float('-inf')
        for i in range(1, len(pre)):
            maxSubSum = max(maxSubSum,pre[i] - pre[minIndex])
            if pre[i] < pre[minIndex]:
                minIndex = i
        return maxSubSum

    def maxSubArrayV2(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        dp = [0]* len(nums)
        dp[0] = nums[0]
        maxSubSum = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i],nums[i] + dp[i-1])
            maxSubSum = max(dp[i],maxSubSum)
        return maxSubSum
