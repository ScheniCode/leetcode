package top;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * <a href="https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-100-liked">199. 二叉树的右视图</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 我的思路：（没用递归）使用链表层次遍历二叉树，添加完一层打个标记，把该层的最后一个节点放入结果集（也可以把每一曾的遍历顺序倒过来，就是把第一个节点存入结果集）
 * <p>
 * 最优解：（递归）深度优先遍历，第一次道达一个深度后把当前节点值存入结果集，注意递归的时候先调右子树确保是每层的最右节点存入结果集
 *
 * @author schnei
 * @since 2026/1/14
 */
public class Solution_199 {
    /**
     * 这个解答是错误的
     *
     * @param root 根节点
     * @return 右视图列表
     */
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        List<TreeNode> treeNodeList = new ArrayList<>();
        treeNodeList.add(root);
        int i = 0;
        int h = 1;
        while (i != treeNodeList.size()) {
            if (i + 1 > Math.pow(2, h) - 1) {
                h++;
            }
            TreeNode node = treeNodeList.get(i);
            if (node != null) {
                treeNodeList.add(node.left);
                treeNodeList.add(node.right);
                if (result.size() < h) {
                    result.add(node.val);
                } else {
                    result.set(h - 1, node.val);
                }
            }
            i++;
        }
        return result;
    }

    public List<Integer> rightSideView_v2(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        LinkedList<TreeNode> treeNodeList = new LinkedList<>();
        treeNodeList.addLast(root);
        treeNodeList.addLast(null);
        int h = 1;
        while (!treeNodeList.isEmpty()) {
            TreeNode node = treeNodeList.removeFirst();
            if (node == null) {
                h++;
                if (!treeNodeList.isEmpty()) {
                    treeNodeList.addLast(null);
                }
            } else {
                if (result.size() < h) {
                    result.add(node.val);
                } else {
                    result.set(h - 1, node.val);
                }
                if (node.left != null) {
                    treeNodeList.addLast(node.left);
                }
                if (node.right != null) {
                    treeNodeList.addLast(node.right);
                }
            }
        }
        return result;
    }
}

// 其他类已经定义过了

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
