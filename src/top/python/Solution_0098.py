# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from CommonType import TreeNode

"""
98. 验证二叉搜索树
https://leetcode.cn/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-100-liked

递归   非最优解  
中序遍历  然后判断严格单调增
"""
# todo   中序遍历  然后判断严格单调增

class Info:
    def __init__(self, isValidBST: bool, min: int, max: int):
        self.isValidBST = isValidBST
        self.min = min
        self.max = max


def getInfo(root: Optional[TreeNode]) -> Optional[Info]:
    if root is None:
        return None
    l_info = getInfo(root.left)
    r_info = getInfo(root.right)
    if l_info is not None and r_info is not None:
        return Info(l_info.isValidBST and r_info.isValidBST and l_info.max < root.val < r_info.min,
                    min(l_info.min, r_info.min, root.val),
                    max(l_info.max, r_info.max, root.val))
    if l_info is not None and r_info is None:
        return Info(l_info.isValidBST and root.val > l_info.max, min(l_info.min, root.val),
                    max(l_info.max, root.val))
    if l_info is None and r_info is not None:
        return Info(r_info.isValidBST and root.val < r_info.min, min(r_info.min, root.val),
                    max(r_info.max, root.val))
    return Info(True, root.val, root.val)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        info = getInfo(root)
        return info.isValidBST


from collections import deque
def build_tree(arr: list) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

if __name__ == '__main__':
    # [5,4,6,null,null,3,7]

    root = build_tree([3,1,5,0,2,4,6,None,None,None,3])
    print(Solution().isValidBST(root))
