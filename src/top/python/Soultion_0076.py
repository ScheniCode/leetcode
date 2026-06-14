"""
76. 最小覆盖子串
https://leetcode.cn/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-100-liked

滑动窗口   用t初始化欠债表 map  总欠债count
count == 0时窗口可覆盖t

然后尝试l是否可以右移 不能则将r右移 再尝试l右移 不断尝试直到s结束

"""


class Solution:
    # 左049 已解决
    def minWindow(self, s: str, t: str) -> str:
        map = {}
        for c in t:
            map[c] = map.get(c, 0) - 1
        count = len(t)
        start = -1
        length = len(s)
        l = r = 0
        while r < len(s):
            r += 1
            if s[r - 1] in map:
                if map[s[r - 1]] < 0 and count > 0:
                    count -= 1
                map[s[r - 1]] +=  1
            if count == 0:
                while (s[l] not in map or map[s[l]] > 0) and l < r:
                    if  s[l] in map:
                        map[s[l]] -= 1
                    l += 1
                if length >= r - l:
                    start = l
                    length = r - l
        if start == -1:
            return ""
        return s[start:start + length]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))