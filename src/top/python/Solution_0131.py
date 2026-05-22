"""
131. 分割回文串
https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked

回文半径   然后回溯算法
"""
from typing import List


def backtrack(param, ss, rr, ans):

    pass


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ss = []
        for c in s:
            ss.append(c)
            ss.append('#')
        ss.pop()
        rr = []
        l = len(ss)
        for i, char in enumerate(ss):
            r = 1
            while i - r >= 0 and i + r < l and ss[i - r] == ss[i + r]:
                r += 1
            rr.append(r)
        ans = []
        return backtrack(0,ss,rr,ans)