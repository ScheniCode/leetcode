"""
239. 滑动窗口最大值
https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked

堆存储滑动窗口数据   堆顶下标小于左边界直接弹出   大于左边界收集
"""
import heapq
from typing import List


class Solution:

    # TODO 看最优解
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(0, k - 1):
            heapq.heappush(window, (-nums[i], i))
        windowMax = []
        for i in range(0, len(nums) - k + 1):
            heapq.heappush(window, (-nums[i + k - 1], i + k - 1))
            val, index = window[0]
            while index < i:
                heapq.heappop(window)
                val, index = window[0]
            windowMax.append(-val)
        return windowMax
