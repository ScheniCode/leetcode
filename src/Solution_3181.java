import java.util.Arrays;

/**
 * <a href="https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/">3181. 执行操作可获得的最大总奖励 II</a>
 * <p>
 * <p>
 * 1 <= rewardValues.length <= 5 * 10^4
 * 1 <= rewardValues[i] <= 5 * 10^4
 *
 * @author schnei
 */
public class Solution_3181 {
    final private static int[][] dp = new int[50001][250001];

    public int maxTotalReward(int[] rewardValues) {
        Arrays.sort(rewardValues);
        Arrays.fill(dp, -1);
        return f(0, 0, rewardValues);
    }

    private int f(int i, int x, int[] rewardValues) {
        if (dp[i][x] != -1) {
            return dp[i][x];
        }
        if (i == rewardValues.length) {
            return x;
        }
        int ans = 0;
        if (x < rewardValues[i]) {
            ans = Math.max(f(i + 1, x + rewardValues[i], rewardValues), f(i + 1, x, rewardValues));

        } else {
            ans = f(i + 1, x, rewardValues);
        }
        dp[i][x] = ans;
        return ans;
    }
}
