"""
22. 括号生成
https://leetcode.cn/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-100-liked

回溯    需要单独记录左右括号的数量
       根据左右括号的数量确认后面是加 "(" 还是 ")"
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.parenthesis(0, 0, "", n, result)
        return result

    def parenthesis(self, l, r, pre, n, result: List[str]):
        if r == n:
            result.append(pre)
            return
        if l == r:
            self.parenthesis(l + 1, r, pre + "(", n, result)
            return
        if l == n:
            self.parenthesis(l, r + 1, pre + ")", n, result)
            return
        if l > r:
            self.parenthesis(l + 1, r, pre + "(", n, result)
            self.parenthesis(l, r + 1, pre + ")", n, result)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
