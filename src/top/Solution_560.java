package top;

/**
 * <a href="https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked">560. 和为 K 的子数组</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 最优解：将所有前缀和存在map中，出现相同的前缀和则出现次数累加，每计算一个前缀和就区去map中找有没有做差之后等于k的值，出现次数累加到计数器上
 * <p>
 * 我的思路：前缀和存在数组中，每次找差为k的前缀每次都要把前面的所有值都遍历一遍；
 *
 * @author schnei
 * @since 2026/1/15
 */
public class Solution_560 {

    public int result = 0;

    public int subarraySum(int[] nums, int k) {
        long[] preSum = new long[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
            for (int j = 0; j <= i; j++) {
                if (preSum[i + 1] - preSum[j] == k) {
                    result++;
                }
            }
        }
        return result;
    }
}
