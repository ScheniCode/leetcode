"""
155. 最小栈
https://leetcode.cn/problems/min-stack/description/?envType=study-plan-v2&envId=top-100-liked

数组模拟栈
再用一个数组存储最小值的索引，栈顶弹出时判断当前最小值是否还在栈中

"""

class MinStack:

    def __init__(self):
        self.arr = []
        self.minIndexArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minIndexArr) == 0:
            self.minIndexArr.append(0)
        elif self.arr[self.minIndexArr[-1]] > val:
            self.minIndexArr.append(len(self.arr)-1)

    def pop(self) -> None:
        self.arr.pop()
        if self.minIndexArr[-1] == len(self.arr):
            self.minIndexArr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.arr[self.minIndexArr[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()