from platform import node
from typing import List

from top.python.CommonType import TreeNode, build_tree

"""
236. 二叉树的最近公共祖先
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-100-liked

找到root到两个节点的路径   最后一个相同的节点就是共同根节点
"""

# TODO AC 但是非最优解   抽空看题解
class Solution:
    def findPath(self, root: TreeNode, p: TreeNode, path: List[TreeNode]):
        path.append(root)
        if root.val == p.val:
            self.path = path.copy()
            return
        if root.left is not None:
            self.findPath(root.left, p, path)
        if root.right is not None:
            self.findPath(root.right, p, path)
        path.pop()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.findPath(root, p, [])
        path_p = self.path
        self.findPath(root, q, [])
        path_q = self.path
        l = min(len(path_q), len(path_p))
        node: TreeNode = root
        for i in range(l):
            if path_p[i].val == path_q[i].val:
                node = path_p[i]
            else:
                break
        return node


if __name__ == '__main__':
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    # path = []
    # findPath(root, TreeNode(5), path)
    print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(4)))
    # print(path)
