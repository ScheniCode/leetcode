import math
from typing import List


"""
169. 多数元素
https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-100-liked

暴力解
"""

# TODO 抽空看最优解
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = nums[0]
        map = {}
        for i in nums:
            count = map.get(i,0)
            map[i] = count+1
        m = math.ceil(len(nums)/2)
        map.keys()
        for k in map.keys():
            if map.get(k) >= m:
                return k
        return n

if __name__ == '__main__':
    print(Solution().majorityElement([1,1,1,1,1,4]))