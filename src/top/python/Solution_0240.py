from typing import List

"""
240. 搜索二维矩阵 II
https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked

两次二分法  第一次搜索每行首列，找到等于目标值的位置或者小与目标值的最大行号  在小于等于这个行号中搜索目标值

"""

# TODO   抽空看最优解


def findMaxRow(target: int, matrix: List[List[int]]) -> int:
    l = 0
    r = len(matrix) - 1
    while l <= r:
        m = l + (r - l) // 2
        if matrix[m][0] >= target:
            r = m
            if r <= l:
                return m
        else:
            l = m + 1
    return len(matrix) - 1


def findMinRow(target: int, matrix: List[List[int]]) -> int:
    l = 0
    r = len(matrix) - 1
    while l <= r:
        m = l + (r - l) // 2
        if matrix[m][-1] >= target:
            r = m
            if r <= l:
                return m
        else:
            l = m + 1
    return -1


def findCol(target: int, arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            return m
    return -1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_row = findMaxRow(target, matrix)
        if max_row == -1:
            return False
        min_row = findMinRow(target, matrix)
        if min_row == -1:
            return False
        for i in range(max_row , min_row - 1, -1):
            col = findCol(target, matrix[i])
            if col >= 0:
                return True
        return False


if __name__ == '__main__':
    matrix = [[-1,3]]

    print(Solution().searchMatrix(matrix, 3))
