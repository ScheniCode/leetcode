# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from top.python.CommonType import ListNode


"""
19. 删除链表的倒数第 N 个结点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-100-liked

两次遍历   一次统计总数  然后计算正序index  遍历删除
"""


# TODO 单次遍历的实现

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0
        while node is not None:
            count+=1
            node = node.next
        node = head
        pre = head
        i = 0
        n = count - n
        while i < n:
            i+=1
            pre = node
            node = node.next
        pre.next = node.next
        if n == 0:
            head = head.next
        return head
