package top;

/**
 * <a href="https://leetcode.cn/problems/find-the-duplicate-number/description/?envType=study-plan-v2&envId=top-100-liked">287. 寻找重复数</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 数组中每个位置的值看做下一个节点的下标，以此来构建链表，因为至少有两个相同的元素，所以生成的链表至少有两个节点指向同一个节段，故生成的链表一定有环；
 *
 * @author schne
 * @since 2026/1/14
 */
public class Solution_287 {

    public static void main(String[] args) {
        System.out.println(0 ^ 5);
    }

    public int findDuplicate(int[] nums) {
        if (nums.length < 2) {
            return -1;
        }
        int s = nums[0];
        int f = nums[s];
        while (s != f) {
            s = nums[s];
            f = nums[nums[f]];
        }
        f = 0;
        while (s != f) {
            s = nums[s];
            f = nums[nums[f]];
        }
        return nums[s];
    }
}
