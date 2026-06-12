"""
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-100-liked
34. 在排序数组中查找元素的第一个和最后一个位置

二分法找左右边界
"""
from typing import List


def findLift(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (r - l) // 2 + l
        if nums[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = findLift(nums, target)
        r = findLift(nums, target+1)
        if l == len(nums):
            return [-1, -1]
        if nums[l] == target:
            return [l, r-1]
        return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
