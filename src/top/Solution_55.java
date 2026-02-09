package top;

/**
 * <a href="https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked">55. 跳跃游戏</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *
 * @author schnei
 * @since 2026/1/22
 */
public class Solution_55 {

    public boolean canJump(int[] nums) {
        int maxIndex = 0;
        for (int i = 0; i <= maxIndex && maxIndex < nums.length-1; i++) {
            maxIndex = Math.max(maxIndex,i+nums[i]);
        }
        return maxIndex >= nums.length -1;
    }
}
