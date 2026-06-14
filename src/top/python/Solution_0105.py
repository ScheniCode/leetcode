"""
105. 从前序与中序遍历序列构造二叉树
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked

递归
先序找到root   然后根据root在中序的index将中序切分成左子树的中序和右子树的中序
--遍历先序  根据上一步的两个数组元素  得到左右子树的先序遍历
不用遍历  直接根据上一步的两个数组数量切分
"""
from typing import List, Optional

from top.python.CommonType import TreeNode


class Solution:
    # 最后一个用例超时了.....
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        index = inorder.index(val)
        leftInorder = inorder[:index]
        rightInorder = inorder[index+1:]
        leftPreorder = preorder[:len(leftInorder)]
        rightPreorder = preorder[len(leftInorder):]
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root



if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    Solution().buildTree(preorder, inorder)