"""
4. 寻找两个正序数组的中位数
https://leetcode.cn/problems/median-of-two-sorted-arrays/submissions/717343957/?envType=study-plan-v2&envId=top-100-liked

归并后直接取中位数
"""
from typing import List

# TODO 看看最优解

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        num = []
        m = len(nums1)
        n = len(nums2)
        while i < m or j < n:
            if j >= n or (i < m and nums1[i] <= nums2[j]):
                num.append(nums1[i])
                i += 1
            elif i >= m or (j < n and nums2[j] < nums1[i]):
                num.append(nums2[j])
                j += 1
        r = (m + n) % 2
        return num[(m + n) // 2] if r == 1 else (num[(m + n) // 2 - 1] + num[(m + n) // 2]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    Solution().findMedianSortedArrays(nums1, nums2)
