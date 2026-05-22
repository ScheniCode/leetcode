"""
108. 将有序数组转换为二叉搜索树
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-100-liked

以中点为root   两边再分别构建子树
"""
from typing import List, Optional

from top.python.CommonType import TreeNode


def buildBST(nums: List[int], lift: int, right: int) -> Optional[TreeNode]:
    if lift > right:
        return None
    if lift == right:
        return TreeNode(nums[lift])
    else:
        index = (right - lift) // 2 + lift
        root = TreeNode(nums[index])
        root.left = buildBST(nums, lift, index - 1)
        root.right = buildBST(nums, index + 1, right)
        return root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return buildBST(nums, 0, len(nums) - 1)
