"""
416. 分割等和子集
https://leetcode.cn/problems/partition-equal-subset-sum/?envType=study-plan-v2&envId=top-100-liked

暴力解 先根据sum的奇偶判断是否有可能分割  然后回溯找到判断是否有解  超时
挂上缓存（dp） 通过
"""
from typing import List

# TODO 看下最优解

def f(index, heaf, nums,dp):
    if heaf == 0:
        dp[index][heaf] = 1
        return True
    if index == len(nums):
        dp[index][heaf] = -1
        return False
    if nums[index] > heaf:
        dp[index][heaf] = -1
        return False
    if dp[index][heaf] != 0:
        return dp[index][heaf] > 0
    b = f(index + 1, heaf, nums,dp) or f(index + 1, heaf - nums[index], nums,dp)
    dp[index][heaf] = 1 if b else -1
    return dp[index][heaf] > 0


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        sum = 0
        for n in nums:
            sum += n
        if sum % 2 == 1:
            return False
        heaf = sum // 2
        dp = [[0] * (heaf + 1) for _ in range(len(nums) + 1)]
        return f(0, heaf, nums, dp)
