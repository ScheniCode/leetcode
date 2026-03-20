"""
234. 回文链表
https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

复制倒序链表 遍历比较 （这方法也太蠢了X）

题解
    复制链表值到数组中 使用双指针法判断是否为回文

    currentNode 指针是先到尾节点，由于递归的特性再从后往前进行比较。frontPointer 是递归函数外的指针。若 currentNode.val != frontPointer.val 则返回 false。反之，frontPointer 向前移动并返回 true

    反转后半部分的链表，然后遍历比较
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from top.python.CommonType import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        copy_head = None
        while node:
            copy_head = ListNode(node.val,copy_head)
            node = node.next
        node = head
        copy_node = copy_head
        while node:
            if not node.val == copy_node.val:
                return False
            node = node.next
            copy_node = copy_node.next
        return True

    def isPalindrome_v2(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

if __name__ == "__main__":
    h = [1, 2, 2, 1]
    head = None
    node = None
    pre = None
    for e in h:
        node = ListNode(e)
        if pre is not None:
            pre.next = node
        pre = node
        if head is None:
            head = node
    print(Solution().isPalindrome(head))

