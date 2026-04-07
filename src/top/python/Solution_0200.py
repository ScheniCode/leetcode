"""
200. 岛屿数量
https://leetcode.cn/problems/number-of-islands/?envType=study-plan-v2&envId=top-100-liked

并查集
"""

from typing import List


# TODO 暴力解 抽空看最优解
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = []
        map = {}
        for i in range(m):
            parent.append([-1] * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                parent[i][j] = i * n + j
                map[parent[i][j]] = [[i, j]]
                if j > 0 and grid[i][j-1] == '1':
                    map.pop(parent[i][j])
                    parent[i][j] = parent[i][j-1]
                    map[parent[i][j]].append([i, j])
                if i > 0 and grid[i-1][j] == '1' and parent[i-1][j] != parent[i][j]:
                    island = map.pop(parent[i][j])
                    for el in island:
                        parent[el[0]][el[1]] = parent[i-1][j]
                        map[parent[i-1][j]].append(el)
        return len(map)


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

    print(Solution().numIslands(grid))