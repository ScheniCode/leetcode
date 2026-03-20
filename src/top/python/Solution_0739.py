"""
739. 每日温度
https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked

单调栈（存下标，比较数组对应位置的值）  小压大   相等也入栈    弹出的时候外面的元素就对应最近的大于栈顶元素的位置

"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        answer = [0] * l
        stack: List[int] = []
        stack.append(0)
        for i in range(1, l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer
