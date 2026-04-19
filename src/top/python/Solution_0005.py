"""
5. 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-100-liked

字符串首尾和字母之间补占位符  然后循环  从每一位向两边比较
"""

# TODO 看下最优解

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str = ['#'] * (2 * len(s) + 1)
        for i in range(len(s)):
            str[2 * i + 1] = s[i]
        max_r = 0
        index = 1
        for i in range(1, len(str) - 1):
            r = 0
            while i - r > 0 and i + r < len(str) - 1:
                if str[i - r - 1] == str[i + r + 1]:
                    r += 1
                else:
                    break
            if r > max_r:
                max_r = r
                index = i
        seq = ''
        for i in range(index - max_r+1, index + max_r, 2):
            seq += str[i]
        return seq

if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))