"""
148. 排序链表
https://leetcode.cn/problems/sort-list/?envType=study-plan-v2&envId=top-100-liked

递归实现归并排序
"""

from typing import Optional

from top.python.CommonType import ListNode
# TODO 看下最优解

def merge(start, end):
    if start == end:
        return
    s = start
    f = start.next
    pre = start
    while True:
        pre = s
        s = s.next
        f = f.next
        if f == end.next or f is None:
            break
        f = f.next
        if f == end.next or f is None:
            break
    m = s
    merge(start, pre)
    merge(m, end)
    arr = []
    f1 = start
    f2 = m
    while f1 != m or f2 != end.next:
        if f1 != m and (f2 == end.next or f1.val <= f2.val):
            arr.append(f1.val)
            f1 = f1.next
        if f2 != end.next and  (f1 == m or f1.val > f2.val):
            arr.append(f2.val)
            f2 = f2.next
    p = start
    for v in arr:
        p.val = v
        p = p.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        while node.next:
            node = node.next
        merge(head, node)
        return head


if __name__ == '__main__':
    arr = [4, 2, 1, 3]
    node = None
    for i in range(len(arr) - 1, -1, -1):
        node = ListNode(arr[i], node)
    Solution().sortList(node)
    while node is not None:
        print(node.val)
        node = node.next
