"""
45. 跳跃游戏 II
https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-100-liked

正向跳跃    每次找到最远点
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        pre = 0
        cur = 0
        next = 0
        count = 0
        while cur < l - 1:
            for i in range(pre,cur+1):
                next = max(next,i + nums[i])
            pre = cur
            cur = next
            count+=1
        return count

if __name__ == '__main__':
    nums =  [2, 3, 0, 1, 4]
    print(Solution().jump(nums))