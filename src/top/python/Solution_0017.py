"""
17. 电话号码的字母组合
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-100-liked

经典回溯算法
"""
from typing import List

num_map = {
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y",'z']
}

def f(index: int, pre: str, s: list[str], result: List[str]):
    if index == len(s):
        result.append(pre)
        return
    for e in num_map.get(s[index]):
        f(index +1,pre+e,s,result)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = list(digits)
        result = []
        f(0, "", s, result)
        return result
