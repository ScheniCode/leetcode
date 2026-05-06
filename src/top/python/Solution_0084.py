"""
84. 柱状图中最大的矩形
https://leetcode.cn/problems/largest-rectangle-in-histogram/?envType=study-plan-v2&envId=top-100-liked

一个区间找到最小值，然后求这个区间最宽的矩形面积  然后最小值的位置左右拆分 分别求最大的矩形面积
"""
from typing import List

import sys

# TODO 超时了  看最优解

def area(heights: List[int], l: int, r: int) -> int:
    if l > r:
        return 0
    index = l
    minHeight = sys.maxsize
    for i in range(l,r+1):
        if heights[i] < minHeight:
            index = i
            minHeight = heights[i]
    return max((r - l + 1) * minHeight,area(heights,l,index-1),area(heights,index+1,r))


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return area(heights, 0, len(heights)-1)

    def largestRectangleAreaV2(self, heights: List[int]) -> int:
        # 单调栈 找到i左侧第一个小于h[i]的位置  i右侧第一个下于h[i]     r-l-1就是以h[i]为高度时的最大宽度
        n = len(heights)
        lift = [0] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            lift[i] = stack[-1] if stack else -1
            stack.append(i)
        area = 0
        for i in range(n):
            area = max((right[i] -lift[i] -1)* heights[i] ,area)
        return  area


if __name__ == '__main__':
    heights = [2, 3]
    print(Solution().largestRectangleAreaV2(heights))