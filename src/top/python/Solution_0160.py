"""
160. 相交链表
https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked

找到两个链表的尾巴   比较是否相等   判断是否相交
如果相交   其中一个链表连成环   快慢指针找到交点
"""
from typing import Optional

from top.python.CommonType import ListNode

# TODO 看下最优解
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        while p is not None and p.next is not None:
            p = p.next
        q = headB
        while q is not None and q.next is not None:
            q = q.next
        if q != p:
            return None
        q.next = headB
        f, s = headA.next.next, headA.next
        while f != s:
            s = s.next
            f = f.next.next
        f = headA
        while f != s:
            s = s.next
            f = f.next
        q.next = None
        return f

if __name__ == '__main__':
    p = ListNode(2,ListNode(3))

    a = ListNode(0,p)
    b = ListNode(1,p)
    q = Solution().getIntersectionNode(a,b)
    print(q)