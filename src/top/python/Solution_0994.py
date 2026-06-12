"""
994. 腐烂的橘子
https://leetcode.cn/problems/rotting-oranges/?envType=study-plan-v2&envId=top-100-liked

暴力解   先遍历一次计算好橘子数量
        每分钟遍历一次处理烂橘子扩撒 查看好橘子数量是否变化  没变化就返回-1  无法全烂
"""
from typing import List


class Solution:
    def orangesRottingV1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    count += 1
        min = 0
        while count > 0:
            pre = count
            preGrid = [a.copy() for a in grid]
            min += 1
            for i in range(0,m):
                for j in range(0,n):
                    if preGrid[i][j] != 2:
                        continue
                    if i > 0 and preGrid[i - 1][j] == 1 and grid[i - 1][j] != 2:
                        grid[i - 1][j] = 2
                        count -= 1
                    if j > 0 and preGrid[i][j - 1] == 1 and grid[i][j - 1] != 2:
                        grid[i][j - 1] = 2
                        count -= 1
                    if i < m - 1 and preGrid[i + 1][j] == 1 and grid[i + 1][j] != 2:
                        grid[i + 1][j] = 2
                        count -= 1
                    if j < n - 1 and preGrid[i][j + 1] == 1 and grid[i][j + 1] != 2:
                        grid[i][j + 1] = 2
                        count -= 1
            if pre == count:
                return -1
        return min

    def orangesRottingV2(self, grid: List[List[int]]) -> int:
        # TODO 广度优先
        pass


if __name__ == '__main__':
    grid = [[0, 1]]
    print(Solution().orangesRotting(grid))
