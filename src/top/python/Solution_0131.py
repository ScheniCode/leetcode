"""
131. 分割回文串
https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked

回文半径   然后回溯算法
"""
from typing import List


# 最优解
# 动态规划  dp[i][j]  标注ij区间是否是会回文
# s[i] == s[j] 且 s[i+1] == s[j-1] 则ij区间是回文

def subStr(ss, star, end):
    s = ''
    for i in range(star, end):
        if ss[i] != '#':
            s += ss[i]
    return s


def backtrack(i, index, ss, rr, container, ans):
    if i == len(ss):
        if index == len(ss):
            ans.append(container.copy())
        return
    if ss[i] == '#' and i == index:
        backtrack(i + 1, index + 1, ss, rr, container, ans)
        return
    if rr[i] - 1 >= i - index:
        r = i - index
        container.append(subStr(ss, index, i + r + 1))
        backtrack(i + r + 1, i + r + 1, ss, rr, container, ans)
        container.pop()
    backtrack(i + 1, index, ss, rr, container, ans)


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
        container = []
        backtrack(0, 0, ss, rr, container, ans)
        return ans


if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
