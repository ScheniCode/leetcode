"""
https://leetcode.cn/problems/word-search/?envType=study-plan-v2&envId=top-100-liked
79. 单词搜索

位置标记   回溯
"""
from typing import List

# TODO 查看最优解

def findWord(n, i, j, board, mark, word):
    if board[i][j] == word[n]:
        mark[i][j] = 1
    else:
        return False
    if n == len(word)-1:
        return True
    if i > 0 and mark[i-1][j] == 0:
        r = findWord(n+1, i-1, j, board, mark, word)
        if r:
            return True
    if j > 0 and mark[i][j-1] == 0:
        r = findWord(n+1, i, j-1, board, mark, word)
        if r:
            return True
    if i < len(board)-1 and mark[i+1][j] == 0:
        r = findWord(n+1, i+1, j, board, mark, word)
        if r:
            return True
    if j < len(board[0])-1 and mark[i][j+1] == 0:
        r = findWord(n+1, i, j+1, board, mark, word)
        if r:
            return True
    mark[i][j] = 0
    return False




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        mark = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if findWord(0, i, j, board, mark, word):
                    return True
        return False

if __name__ == '__main__':
    board =[["a"]]
    word = "a"
    print(Solution().exist(board, word))