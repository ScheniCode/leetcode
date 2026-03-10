from ast import List


"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked

"""
class Solution:
    # TODO 后面重写

    def longestConsecutive(self, nums: List[int]) -> int:
        max = nums[0]
        for i in nums:
            if max < i:
                max = i
