from typing import List

"""
56. 合并区间
https://leetcode.cn/problems/merge-intervals/?envType=study-plan-v2&envId=top-100-liked

暴力解 排序后通过遍历找到重叠区间的左右端点



"""
# todo 非最优解

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = []
        l = intervals[0][0]
        r = intervals[0][1]
        for el in intervals[1::]:
            if el[0] <= r:
                r = max(r, el[1])
            else:
                result.append([l, r])
                l = el[0]
                r = el[1]
        result.append([l, r])
        return result
