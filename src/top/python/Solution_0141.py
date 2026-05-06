"""
141. 环形链表
https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-100-liked

快慢指针
"""
from typing import Optional

from top.python.CommonType import ListNode

 # TODO 抽空看最优解

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        s = head.next
        if s is None:
            return False
        f = head.next.next
        if f is None:
            return False
        while s != f:
            s = s.next
            if s is None:
                return False
            if f.next is None:
                return False
            f = f.next.next
            if f is None:
                return False
        return True

# 将f指针充重置到头部当s、f再次相等时就是相交的节点