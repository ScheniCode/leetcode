"""
46. 全排列
https://leetcode.cn/problems/permutations/?envType=study-plan-v2&envId=top-100-liked

动态规划  使status的二进制位与nums下标对应   0表示未选择   1表示已选择
"""
from typing import List


def f(status: int, pre: List[int], nums: List[int], result: List[List[int]]):
    if status == (1 << len(nums)) - 1:
        result.append(pre.copy())
        return
    for i in range(len(nums)):
        if status & (1 << i) == 0:
            pre.append(nums[i])
            f(status + (1 << i), pre, nums, result)
            pre.pop()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        f(0, [], nums, result)
        return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
