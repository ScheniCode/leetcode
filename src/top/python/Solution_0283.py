from typing import List


"""
283. 移动零
https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=top-100-liked

遍历 遇到0就把后面的元素往前移动   然后末尾补0


"""

# TODO 抽空看最优解

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                index += 1
                if index != i:
                    nums[index] = nums[i]
        if index+1 <= len(nums) - 1:
            for j in range(index+1,len(nums)):
                nums[j] = 0


if __name__ == '__main__':
    nums = [1]
    Solution().moveZeroes(nums)
    print(nums)