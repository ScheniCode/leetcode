from typing import List

"""
54. 螺旋矩阵
https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-100-liked


注意边界条件不断循环
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lift = 0
        right = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1
        result = []
        i, j = 0, 0
        l = len(matrix) * len(matrix[0])
        while True:
            top += 1
            while j <= right:
                result.append(matrix[i][j])
                if len(result) == l:
                    return result
                j += 1
            j -= 1
            right -= 1
            i += 1
            while i <= down:
                result.append(matrix[i][j])
                if len(result) == l:
                    return result
                i += 1
            down -= 1
            i -= 1
            j -= 1
            while j >= lift:
                result.append(matrix[i][j])
                if len(result) == l:
                    return result
                j -= 1
            j += 1
            lift += 1
            i -= 1
            while i >= top:
                result.append(matrix[i][j])
                if len(result) == l:
                    return result
                i -= 1
            j += 1
            i+=1
