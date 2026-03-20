"""
15. 三数之和
https://leetcode.cn/problems/3sum/?envType=study-plan-v2&envId=top-100-liked

暴力解 穷举

"""
from typing import Any


# todo 查看最优解  暴力解超时了

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        up: list[int] = []
        zero: list[int] = []
        low: list[int] = []
        for num in nums:
            if num > 0:
                up.append(num)
            if num < 0:
                low.append(num)
            if num == 0:
                zero.append(0)
        result: list[list[int]] = []
        if len(zero) >= 3:
            result.append([0, 0, 0])
        if len(up) == 0 or len(low) == 0:
            return result
        up.sort()
        low.sort()
        for i, a in enumerate(up):
            for j, b in enumerate(low):
                c = a + b
                if c == 0:
                    if len(zero) > 0 and (len(result) == 0 or not any([b, 0, a] == u for u in result)):
                        result.append([b, 0, a])
                elif c > 0:
                    for index in range(j + 1, len(low)):
                        if low[index] == -c and (len(result) == 0 or not any([b, -c, a] == u for u in result)):
                            result.append([b, -c, a])
                else:
                    for index in range(i + 1, len(up)):
                        if up[index] == -c and (len(result) == 0 or not any([b, a, -c] == u for u in result)):
                            result.append([b, a, -c])
        return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))

