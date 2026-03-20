from typing import List

"""
31. 下一个排列
https://leetcode.cn/problems/next-permutation/?envType=study-plan-v2&envId=top-100-liked

左边的「较小数」与一个右边的「较大数」交换
这个「较小数」尽量靠右，而「较大数」尽可能小

"""
# todo 看题解做的

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(l - 1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i - 1] = nums[i - 1] ^ nums[j]
                        nums[j] = nums[i - 1] ^ nums[j]
                        nums[i - 1] = nums[i - 1] ^ nums[j]
                        break
                for k in range(i,i + int((l - i)/2)):
                    nums[k] = nums[k] ^ nums[l-1-(k-i)]
                    nums[l-1-(k-i)] = nums[k] ^ nums[l-1-(k-i)]
                    nums[k] = nums[k] ^ nums[l-1-(k-i)]
                return
        for i in range(int(l / 2)):
            nums[i] = nums[i] ^ nums[l-i-1]
            nums[l-i-1] = nums[i] ^ nums[l-i-1]
            nums[i] = nums[i] ^ nums[l-i-1]

if __name__ == "__main__":
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    print(nums)
