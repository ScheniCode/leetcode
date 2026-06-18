"""
25. K 个一组翻转链表
https://leetcode.cn/problems/reverse-nodes-in-k-group/submissions/731501418/?envType=study-plan-v2&envId=top-100-liked

暴力解 k个一组逆序    记录下头（逆序后的尾）
"""
from typing import Optional

from top.python.CommonType import ListNode

# TODO 看下最优解

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        pre = None
        node = head
        next = node.next
        kHead = None
        prekHead = None
        kCount = 0
        count = 0
        while node is not None:
            count+=1
            node = node.next
        node = head
        while node is not None:
            kCount += 1
            count -= 1
            if kCount == 1:
                prekHead = kHead
                kHead = node
            if kCount == k:
                kCount = 0
                if prekHead is None:
                    head = node
                if prekHead is not None:
                    prekHead.next = node
            node.next = pre
            pre = node
            node = next
            if node is not None:
                next = node.next
            if kCount == 0 and count < k:
                kHead.next = node
                break
        return head



