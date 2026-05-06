"""
11. 盛最多水的容器
https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked


暴力解  n^2   超时了...
"""
from typing import List


class Solution:
    # 超时了
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = len(height)
        for i in range(0, l - 1):
            for j in range(i + 1, l):
                area = max(area, (j - i) * min(height[i], height[j]))
        return area

    # 最优解  双指针贪心
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return area
