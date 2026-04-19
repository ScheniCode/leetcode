"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/?envType=study-plan-v2&envId=top-100-liked

用栈存左括号  遇到右括号弹出   判断是否匹配
"""
class Solution:
    def isValid(self, s: str) -> bool:
        str = list(s)
        stack = []
        for c in str:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            if not stack:
                return False
            if c == ')' :
                top = stack.pop()
                if top != '(':
                    return False
            if c == ']' :
                top = stack.pop()
                if top != '[':
                    return False
            if c == '}' :
                top = stack.pop()
                if top != '{':
                    return False
        return not stack

if __name__ == '__main__':
    s = "()[]{}"
    Solution().isValid(s)

