"""
21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-100-liked


"""
from typing import Optional

from top.python.CommonType import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        p = list1
        q = list2
        head = None
        cur = None
        tial = None
        while p is not None or q is not None:
            if p is None and q is not None:
                cur = q
                q = q.next
            if q is None and p is not None:
                cur = p
                p = p.next
            if p is not None and q is not None:
                if p.val <= q.val:
                    cur = p
                    p = p.next
                else:
                    cur = q
                    q = q.next
            if head is None:
                head = cur
                tial = cur
            tial.next = cur
            tial = cur
        return head
