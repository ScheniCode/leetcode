"""
41. 缺失的第一个正数
https://leetcode.cn/problems/first-missing-positive/?envType=study-plan-v2&envId=top-100-liked

[0，l)是排好的位置  (r,..)是垃圾区
判断nums[i] == i+1  否则就往后换位置

"""
from typing import List


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]



class Solution:
    # 左050 已解决
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[l] == l+1:
                l+=1
                continue
            if nums[l] < l+1 or nums[l] > r+1 or nums[nums[l]-1] == nums[l]:
                swap(nums,l,r)
                r-=1
            else:
                swap(nums,l,nums[l]-1)
        return l+1

if __name__ == "__main__":
    nums = [1, 2, 0]
    print(Solution().firstMissingPositive(nums))