"""
153. 寻找旋转排序数组中的最小值
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-100-liked


二分法
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while True:
            m = l + (r - l) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[l] < nums[m]:
                l = m
            else:
                break
        return nums[r]
