package top.java;

/**
 * <a href="https://leetcode.cn/problems/reverse-linked-list/?envType=study-plan-v2&envId=top-100-liked">206. 反转链表</a>
 * <p>
 * <p>
 * 调整指针前用变量存储好前一个和后一个节点
 * <p>
 * <p>
 *
 * @author schnei
 * @since 2026/2/15
 */
public class Solution_0206 {

    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode pre = null;
        ListNode next = null;
        while (cur != null) {
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
}
