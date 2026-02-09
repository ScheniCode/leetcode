package top;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <a href="https://leetcode.cn/problems/subsets/?envType=study-plan-v2&envId=top-100-liked">78. 子集</a>
 * <p>
 * <p>
 * <p>
 *
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 * nums 中的所有元素 互不相同
 *
 * <p>
 * <p>
 * <p>
 *  回溯算法的关键是回退这一步
 *
 * @author schne
 * @since 2026/1/13
 */
public class Solution_78 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        List<List<Integer>> subsets = new Solution_78().subsets(nums);
        System.out.println(subsets);
    }


    public List<List<Integer>> subsets(int[] nums) {
        ArrayList<List<Integer>> result = new ArrayList<>();
        f(0, nums, result, new ArrayList<>());
        return result;
    }

    private void f(int i, int[] nums, ArrayList<List<Integer>> result, List<Integer> integers) {
        if (i == nums.length) {
            result.add(List.copyOf(integers));
            return;
        }
        f(i + 1, nums, result, integers);
        integers.add(nums[i]);
        f(i + 1, nums, result, integers);
        integers.removeLast();
    }
}
