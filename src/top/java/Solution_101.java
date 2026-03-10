package top.java;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * <a href="https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked">101. 对称二叉树</a>
 * <p>
 * <p>
 *   暴力解 层次遍历后单独判断改层是否对称
 * <p>
 * <p>
 *     最优解：每一个互为镜象的节点  左侧的左子节点与右侧的右子节点互为镜像  左侧的右子节点与右侧的左子节点互为镜像
 *
 * @author schnei
 * @since 2026/1/26
 */
public class Solution_101 {
    public static void main(String[] args) {
        TreeNode node = new TreeNode(1, new TreeNode(0, null, null), null);
        boolean symmetric = new Solution_101().isSymmetric(node);
        System.out.println(symmetric);
    }


    // 层次遍历后单独判断改层是否对称

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        List<TreeNode> pre = new ArrayList<>();
        List<TreeNode> cur = new ArrayList<>();
        pre.add(root);
        boolean isAllNull = true;
//        for (TreeNode node : pre) {
//            if (node == null){
//                cur.add(null);
//                cur.add(null);
//                continue;
//            }
//            if (node.left != null || node.right != null) {
//                isAllNull = false;
//            }
//            cur.add(node.left);
//            cur.add(node.right);
//        }
        do {
            if (!check(pre)) {
                return false;
            }
            isAllNull = true;
            for (TreeNode node : pre) {
                if (node == null) {
                    cur.add(null);
                    cur.add(null);
                    continue;
                }
                if (node.left != null || node.right != null) {
                    isAllNull = false;
                }
                cur.add(node.left);
                cur.add(node.right);
            }
            pre.clear();
            pre.addAll(cur);
            cur.clear();
        } while (!isAllNull);
        return true;
    }

    private boolean check(List<TreeNode> cur) {
        int size = cur.size();
        if (size == 0 || size == 1) {
            return true;
        }
        for (int i = 0; i < size / 2; i++) {
            if (!eq(cur.get(i), cur.get(size - 1 - i))) {
                return false;
            }
        }
        return true;
    }

    private boolean eq(TreeNode a, TreeNode b) {
        if (a == b) {
            return true;
        }
        if (a != null && b != null) {
            return Objects.equals(a.val, b.val);
        }
        return false;
    }
}
