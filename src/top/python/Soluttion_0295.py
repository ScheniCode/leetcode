"""
295. 数据流的中位数
https://leetcode.cn/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-100-liked

findMedian 二分查找 插入排序     超时了

两个堆维护大于mid的和小于mid的
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        index = self.__find__(num)
        self.arr.append(num)
        while index < len(self.arr):
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            index += 1

    def __find__(self, num: int) -> int:
        l = 0
        r = len(self.arr)
        while l < r:
            mid = l + (r - l) // 2
            if self.arr[mid] <= num:
                l = mid + 1
            else:
                r = mid
        return l

    def findMedian(self) -> float:
        length = len(self.arr)
        mid = length // 2
        if length % 2 == 0:
            return (self.arr[mid - 1] + self.arr[mid]) / 2
        else:
            return self.arr[mid]


class MedianFinderV2:

    def __init__(self):
        self.leftMid = []
        self.rightMid = []

    def addNum(self, num: int) -> None:
        if not self.leftMid or -self.leftMid[0] > num:
            heapq.heappush(self.leftMid, -num)
        else:
            heapq.heappush(self.rightMid, num)
        if len(self.leftMid) > len(self.rightMid) + 1:
            heapq.heappush(self.rightMid,-heapq.heappop(self.leftMid))
        if len(self.leftMid) < len(self.rightMid):
            heapq.heappush(self.leftMid, -heapq.heappop(self.rightMid))

    def findMedian(self) -> float:
        if len(self.leftMid) == len(self.rightMid):
            return (-self.leftMid[0] + self.rightMid[0])/2
        return -self.leftMid[0]


if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(2)
    m.addNum(1)
    m.addNum(3)
    m.addNum(0)
    print(m.findMedian())
