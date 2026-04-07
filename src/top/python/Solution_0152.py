"""
152. 乘积最大子数组
https://leetcode.cn/problems/maximum-product-subarray/?envType=study-plan-v2&envId=top-100-liked

动态归回   dp以i位置结尾的最大前缀积和最小前缀积
"""

from typing import List


#   TODO 需要复习

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        min_num, max_num = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_min = min(nums[i], nums[i] * min_num, nums[i] * max_num)
            cur_max = max(nums[i], nums[i] * min_num, nums[i] * max_num)
            min_num = min(cur_min, nums[i])
            max_num = max(cur_max, nums[i])
            ans = max(max_num, ans)
        return ans
