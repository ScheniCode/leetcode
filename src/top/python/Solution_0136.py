"""
136. 只出现一次的数字
https://leetcode.cn/problems/single-number/description/?envType=study-plan-v2&envId=top-100-liked

异或运算
"""
from typing import List

# TODO 之前两次都没想到

class Solution:
    # 两个相同的数异或等于0
    # 一个数异或0等于自己
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for n in nums:
            num ^= n
        return num

