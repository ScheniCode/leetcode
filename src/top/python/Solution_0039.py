"""
39. 组合总和
https://leetcode.cn/problems/combination-sum/?envType=study-plan-v2&envId=top-100-liked

动态规划  背包问题   递归回溯解法
"""
from typing import List

targetList = []


def f(n, candidates, target, container):
    if target == 0:
        targetList.append(container.copy())
        return
    if n == len(candidates) or target < 0:
        return
    container.append(candidates[n])
    f(n, candidates, target - candidates[n], container)
    container.pop()
    f(n + 1, candidates, target, container)


# TODO  看下状态转移解法

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        targetList.clear()
        container = []
        f(0, candidates, target, container)
        return targetList
