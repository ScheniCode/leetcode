"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked

"""
# TODO 后面重写
from typing import List

# TODO 这解法是最长子序列........

def find(arr, h, i):
    l = 0
    r = h - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > i:
            r = m
            if l == m:
                return m
        else:
            l = m + 1
    return -1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        h = 0
        for i in nums:
            # if h == 0:
            #     arr[0] = i
            #     h += 1
            index = find(arr, h, i)
            if index == -1:
                arr[h] = i
                h += 1
            else:
                arr[index] = i
        return h


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))