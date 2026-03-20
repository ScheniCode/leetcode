"""
124. 二叉树中的最大路径和
https://leetcode.cn/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-100-liked

递归，计算以传入节点为根节点的树[从根阶节点出发的最长路径，整棵树的最长路径]，之后返回到上一级继续处理，注意值小于0的节点
TODO 有空看下最优解
"""
from typing import Optional

from top.python.common import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        info = self.childPath(root)
        return max(info[0], info[1])

    def childPath(self, node: Optional[TreeNode]) -> list[int]:
        result = [0, 0]
        left_info = [0, 0]
        right_info = [0, 0]
        if node.left is not None:
            left_info = self.childPath(node.left)
            result[0] = node.val + max(0, left_info[0])
            result[1] = max(result[0], left_info[1])
            if node.right is None:
                return result
        if node.right is not None:
            right_info = self.childPath(node.right)
            result[0] = node.val + max(0, right_info[0])
            result[1] = max(result[0], right_info[1])
            if node.left is None:
                return result
        if node.left is None and node.right is None:
            return [node.val, node.val]
        result[0] = node.val + max(0, left_info[0], right_info[0])
        result[1] = max(node.val + max(0, left_info[0]) + max(0, right_info[0]), max(left_info[1], right_info[1]),
                        result[0])
        return result


if __name__ == "__main__":
    # root = TreeNode(2)
    # root.left = TreeNode(-1)
    # print(Solution().maxPathSum(root))
    # root = TreeNode(-1, TreeNode(-2, TreeNode(-6)), TreeNode(10, TreeNode(-3), TreeNode(-6)))
    # print(Solution().maxPathSum(root))
    root = TreeNode(-6, right=TreeNode(3,TreeNode(2)))
    print(Solution().maxPathSum(root))
