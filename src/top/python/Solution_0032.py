"""
32. 最长有效括号
https://leetcode.cn/problems/longest-valid-parentheses/?envType=study-plan-v2&envId=top-100-liked


"""


class Solution:
    """"
    从左到右遍历处理不了这个场景    s = "))))((()(("
    再从右到左遍历一次就可以覆盖了

    sum拆开独立计数左右括号
    """

    def longestValidParentheses1(self, s: str) -> int:
        sum = 0
        queue = []
        length = 0
        for c in s:
            queue.append(c)
            if c == '(':
                sum += 1
            if c == ')':
                sum -= 1
            if sum < 0:
                queue.clear()
                sum = 0
            if sum == 0:
                length = max(len(queue), length)
        while sum > 0 and queue:
            first = queue.pop(0)
            if first == '(':
                sum -= 1
            if first == ')':
                sum += 1
        if queue and queue[0] == '(':
            length = max(len(queue), length)
        return length

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = max(length, i - stack[-1])
        return length


if __name__ == '__main__':
    s = "))))((()(("
    print(Solution().longestValidParentheses(s))
