package top;

/**
 * <a href="https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked">543. 二叉树的直径</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * <p>
 * V1：暴力递归需要要重复算深度
 * <p>
 * 最优解：实际一次求圣都的递归就可以解决，用一个变量存最大直径，不断去更新
 *
 * @author schnei
 * @since 2026/1/16
 */
public class Solution_543 {
    int maxDiameter = 0;

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2, null, null), null);
        int i = new Solution_543().diameterOfBinaryTree_V2(root);
        System.out.println(i);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = 0;
        if (root.left != null) {
            l = 1 + deep(root.left);
        }
        int r = 0;
        if (root.right != null) {
            r = 1 + deep(root.right);
        }

        return Math.max(l + r, Math.max(diameterOfBinaryTree(root.right), diameterOfBinaryTree(root.left)));
    }

    private int deep(TreeNode node) {
        if (node == null || (node.right == null && node.left == null)) {
            return 0;
        }
        return 1 + Math.max(deep(node.left), +deep(node.right));
    }


    public int diameterOfBinaryTree_V2(TreeNode root) {
        root.val = h(root);
        return diameter(root);
    }

    private int diameter(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = 0;
        if (root.left != null) {
            l = 1 + root.left.val;
        }
        int r = 0;
        if (root.right != null) {
            r = 1 + root.right.val;
        }
        return Math.max(l + r, Math.max(diameter(root.right), diameter(root.left)));
    }

    private int h(TreeNode node) {
        if (node == null) {
            return 0;
        }
        if (node.right == null && node.left == null) {
            node.val = 0;
            return 0;
        }
        int h = 1 + Math.max(h(node.left), +h(node.right));
        node.val = h;
        return h;
    }
}
