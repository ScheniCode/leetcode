"""
<a href="https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-100-liked">215. 数组中的第K个最大元素</a>

偷懒的做法 排序后取对应的下标

最优解：随机快排的思路，随机选定一个数，荷兰国旗划分，然后看中间的区间边界决定从左边partition还是右边partition

"""


class Solution:
    def findKthLargest(self, nums, k) -> int:
        nums.sort()
        return nums[-k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
