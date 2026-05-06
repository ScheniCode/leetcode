"""
114. 二叉树展开为链表
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

递归先序遍历
"""
from typing import Optional

from top.python.CommonType import TreeNode

# TODO 最优解  用栈遍历
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)
        root.left = None
        if left is not None:
            root.right = left
            end = left
            while end.right is not None:
                end = end.right
            end.right = right