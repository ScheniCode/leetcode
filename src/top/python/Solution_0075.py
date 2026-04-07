"""
75. 颜色分类
https://leetcode.cn/problems/sort-colors/?envType=study-plan-v2&envId=top-100-liked

荷兰国旗问题
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        i = 0
        while i < r:
            if nums[i] == 0:
                l += 1
                if l != i:
                    nums[l] = nums[l] ^ nums[i]
                    nums[i] = nums[l] ^ nums[i]
                    nums[l] = nums[l] ^ nums[i]
                    continue
            if nums[i] == 2:
                r -= 1
                if r != i:
                    nums[r] = nums[r] ^ nums[i]
                    nums[i] = nums[r] ^ nums[i]
                    nums[r] = nums[r] ^ nums[i]
                    continue
            i += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
