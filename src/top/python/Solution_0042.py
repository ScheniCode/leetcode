"""
42. 接雨水
https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-100-liked

从左遍历找比左边界高的   累加
从右遍历找比右边界高的   累加
"""
from typing import List

# TODO  看最优解

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        sum = 0
        for i in range(1, len(height)):
            if height[i] >= height[l]:
                h = min(height[i],height[l])
                for index in range(l+1,i):
                    sum += (h-height[index])
                l = i
        l = len(height)-1
        for i in range(len(height)-2, -1, -1):
            if height[i] > height[l]:
                h = min(height[i],height[l])
                for index in range(i+1,l):
                    sum += (h-height[index])
                l = i
        return sum


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))