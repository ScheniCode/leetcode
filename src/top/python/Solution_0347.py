"""
347. 前 K 个高频元素
https://leetcode.cn/problems/top-k-frequent-elements/?envType=study-plan-v2&envId=top-100-liked

暴力解  统计词频    排序   top k

"""
from typing import List

# 看下最优解   items.sort换成堆实际就是最优解了   size = k的堆  遍历完就是最终结果

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            count = map.get(num, 0)
            map[num] = count + 1
        items = []
        for key in map.keys():
            items.append([key, map[key]])
        items.sort(key=lambda a: a[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(items[i][0])
        return ans

if __name__ == '__main__':
    nums = [1]
    k = 1
    print(Solution().topKFrequent(nums, k))

