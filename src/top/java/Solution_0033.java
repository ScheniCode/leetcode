package top.java;

/**
 * <a href="https://leetcode.cn/problems/search-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-100-liked">33. 搜索旋转排序数组</a>
 * <p>
 * <p>
 *  两次二分，第一次找的k的位置，第二次以k为起始位置二分找target
 * <p>
 * <p>
 *
 * @author schnei
 * @since 2026/2/14
 */
public class Solution_0033 {

    public static void main(String[] args) {
        int[] ints = new int[]{4,5,6,7,0,1,2};
        int search = new Solution_0033().search(ints, 3);
        System.out.println(search);
    }

    public int search(int[] nums, int target) {
        int length = nums.length;
        if (length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        int k = findK(nums);
        int l = 0;
        int r = nums.length - 1;
        int m;
        while (l <= r) {
            m = l + (r - l) / 2;
            int index = (m + k) % length;
            if (nums[index] == target) {
                return index;
            } else if (nums[index] > target) {
                r = m-1;
            } else {
                l = m+1;
            }
        }
        return -1;
    }

    private int findK(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int m;
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
