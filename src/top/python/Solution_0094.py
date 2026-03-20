"""
94. 二叉树的中序遍历
https://leetcode.cn/problems/binary-tree-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked

递归   下午看看迭代实现

"""
from typing import Optional, List

from top.python.CommonType import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        if root.left is not None:
            for e in self.inorderTraversal(root.left):
                result.append(e)
        result.append(root.val)
        if root.right is not None:
            for e in self.inorderTraversal(root.right):
                result.append(e)
        return result

    def inorderTraversal_v2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        my_stack = []
        node: TreeNode = root
        while my_stack or node is not None:
            if node is not None:
                my_stack.append(node)
                node = node.left
            else:
                node = my_stack.pop()
                result.append(node.val)
                node = node.right
        return result


if __name__ == '__main__':
    if [1]:
        print("null")