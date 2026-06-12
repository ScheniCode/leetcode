"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked

排序后遍历    判断是否连续    记录最大长度
"""
from typing import List

# TODO 看看最优解

# 这解法是最长子序列........

# def find(arr, h, i):
#     l = 0
#     r = h - 1
#     while l <= r:
#         m = l + (r - l) // 2
#         if arr[m] > i:
#             r = m
#             if l == m:
#                 return m
#         else:
#             l = m + 1
#     return -1


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     arr = [0] * len(nums)
    #     h = 0
    #     for i in nums:
    #         # if h == 0:
    #         #     arr[0] = i
    #         #     h += 1
    #         index = find(arr, h, i)
    #         if index == -1:
    #             arr[h] = i
    #             h += 1
    #         else:
    #             arr[index] = i
    #     return h

    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        nums.sort()
        pre = nums[0]
        l = 1
        maxLength = 1
        for i in range(1, length):
            if nums[i] == pre + 1:
                l += 1
            elif nums[i] != pre:
                l = 1
            pre = nums[i]
            maxLength = max(l, maxLength)
        return maxLength


if __name__ == '__main__':
    nums =  [1, 0, 1, 2]
    print(Solution().longestConsecutive(nums))
