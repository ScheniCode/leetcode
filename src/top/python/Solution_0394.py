"""
394. 字符串解码
https://leetcode.cn/problems/decode-string/submissions/704132175/?envType=study-plan-v2&envId=top-100-liked

递归
遇到 [ 调函数
遇到 ] 返回

"""
class Solution:
    def __init__(self):
        self.index = None

    def decodeString(self, s: str) -> str:
        var = list(s)
        return self.f(var, 0)

    def f(self, char: list[str], i: int) -> str:
        path = ""
        count = None
        while i < len(char):
            if ord("a") <= ord(char[i]) <= ord("z"):
                path += char[i]
            if ord("0") <= ord(char[i]) <= ord("9"):
                if count is None:
                    count = int(char[i])
                else:
                    count = 10 * count + int(char[i])
            if char[i] == "[":
                if count is None:
                    count = 1
                path += count * self.f(char, i + 1)
                i = self.index
                count = None
                continue
            if char[i] == "]":
                self.index = i+1
                return path
            i += 1
        return path


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
