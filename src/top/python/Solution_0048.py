"""
https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-100-liked
48. 旋转图像

由内而外   一圈一圈处理  内层循环注意不要带上最后一个元素
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        star = n // 2 - 1
        while star >= 0:
            a = n - 2 * star
            for i in range(a - 1):
                temp = matrix[star][star + i]
                matrix[star][star + i] = matrix[star + a - i - 1][star]
                matrix[star + a - i - 1][star] = matrix[star + a - 1][star + a - i - 1]
                matrix[star + a - 1][star + a - i - 1] = matrix[star + i][star + a - 1]
                matrix[star + i][star + a - 1] = temp
            star -= 1


if __name__ == '__main__':
    l = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    print(matrix)
