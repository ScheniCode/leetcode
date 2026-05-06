"""
2. 两数相加
https://leetcode.cn/problems/add-two-numbers/?envType=study-plan-v2&envId=top-100-liked

注意考虑进位
"""
from typing import Optional

from top.python.CommonType import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        result = ListNode(0)
        pre = None
        cur = result
        while p1 is not None or p2 is not None:
            if p1 is not None:
                cur.val += p1.val
                p1 = p1.next
            if p2 is not None:
                cur.val += p2.val
                p2 = p2.next
            cur.next = ListNode()
            if cur.val > 9:
                cur.next.val = cur.val // 10
                cur.val = cur.val % 10
            pre = cur
            cur = cur.next
        if pre is not None and cur.val == 0:
            pre.next = None
        return result
