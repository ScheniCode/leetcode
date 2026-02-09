package top;

import java.util.HashSet;
import java.util.Set;

/**
 * <a href="https://leetcode.cn/problems/path-sum-iii/description/?envType=study-plan-v2&envId=top-100-liked">437. 路径总和 III</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 深度优先遍历，计算路径
 * <p>
 * 最优解：把前缀路径和缓存到map中，避免重复计算
 * <p>
 * 我的思路：递归计算路径，前缀路径有大量重复计算
 *
 * @author schnei
 * @since 2026/1/15
 */
public class Solution_437 {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, null, new TreeNode(2, null, new TreeNode(3, null, new TreeNode(4, null, new TreeNode(5, null, null)))));

        int i = new Solution_437().pathSum(root, 3);
        System.out.println(i);
    }


    public Set<TreeNode> start = new HashSet<>();
    public int count = 0;

    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return 0;
        }
        start.add(root);
        dfs(root, 0, root, targetSum);
        return count;
    }

    private void dfs(TreeNode node, long sum, TreeNode head, int targetSum) {
        if (sum + node.val == targetSum) {
            count++;
        }
        if (node.left != null) {
            dfs(node.left, sum + node.val, head, targetSum);
            if (!start.contains(node.left)) {
                start.add(node.left);
                dfs(node.left, 0, node.left, targetSum);
            }
        }
        if (node.right != null) {
            dfs(node.right, sum + node.val, head, targetSum);
            if (!start.contains(node.right)) {
                start.add(node.right);
                dfs(node.right, 0, node.right, targetSum);
            }
        }
    }
}
