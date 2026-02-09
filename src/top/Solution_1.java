package top;

import java.util.Arrays;
import java.util.HashMap;

/**
 * <a href="https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked">1. 两数之和</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *
 * @author schnei
 * @since 2026/1/20
 */
public class Solution_1 {

    // TODO 明天看下最优解
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            Integer val = map.get(nums[i]);
            if (val == null) {
                map.put(nums[i], i);
            } else if (2 * nums[i] == target) {
                result[0] = val;
                result[1] = i;
                return result;
            } else {
                map.remove(nums[i]);
            }
        }
        for (int i = 0; i < nums.length; i++) {
            Integer val = map.get(target - nums[i]);
            if (val != null && !val.equals(i)) {
                result[0] = i;
                result[1] = val;
                break;
            }
        }
        return result;
    }
}
