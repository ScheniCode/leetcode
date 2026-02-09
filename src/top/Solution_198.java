package top;

/**
 * <a href="https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=top-100-liked">198. 打家劫舍</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 一维动态规划模板题目
 * 定义dp[i]是到i位置为止的最大收益，然后比较要i位置和不要i位置的最大值
 *
 * @author schnei
 * @since 2026/1/22
 */
public class Solution_198 {

    // 动态规划


    public int rob(int[] nums) {
        int[] dp = new int[nums.length + 1];
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        return dp[nums.length - 1];
    }
}
