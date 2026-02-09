package top;

/**
 * <a href="https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked">230. 二叉搜索树中第 K 小的元素</a>
 * <p>
 * <p>
 *
 * 树中的节点数为 n 。
 * 1 <= k <= n <= 104
 * 0 <= Node.val <= 104
 *
 * <p>
 * <p>
 *
 *     搜索二叉树中序遍历就是从小到大排列，每访问一个节点就进行计数，到达目标序列后记录下来
 *
 * @author schnei
 * @since 2026/1/15
 */
public class Solution_230 {
    public int i = 0;
    public int result = -1;

    public int kthSmallest(TreeNode root, int k) {
        visit(root, k);
        return result;
    }

    private void visit(TreeNode node, int k) {
        if (node.left != null) {
            visit(node.left, k);
        }
        i++;
        if (i == k) {
            result = node.val;
        }
        if (node.right != null) {
            visit(node.right, k);
        }
    }
}
