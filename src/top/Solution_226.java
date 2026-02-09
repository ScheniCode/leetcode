package top;

import java.util.Stack;

/**
 * <a href="https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked">226. 翻转二叉树</a>
 * <p>
 * <p>
 * 树中节点数目范围在 [0, 100] 内
 * -100 <= Node.val <= 100
 *
 * <p>
 * <p>
 * 遍历整个树，将每个节点的左右叶子节点交换
 *
 * @author schnei
 */
public class Solution_226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);
        while (!stack.empty()) {
            TreeNode top = stack.pop();
            TreeNode left = top.left;
            TreeNode right = top.right;
            if (left != null) {
                stack.add(left);
            }
            if (right != null) {
                stack.add(right);
            }
            top.left = right;
            top.right = left;
        }
        return root;
    }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

