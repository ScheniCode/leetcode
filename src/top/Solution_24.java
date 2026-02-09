package top;

/**
 * <a href="https://leetcode.cn/problems/swap-nodes-in-pairs/?envType=study-plan-v2&envId=top-100-liked">24. 两两交换链表中的节点</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *     两两一组交换节点，注意处理好边界条件避免空指针，还要记录每一组节点的前一个节点，毕竟是单向链表
 *
 * @author schnei
 * @since 2026/1/15
 */
public class Solution_24 {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode f = head;
        ListNode s = head.next;
        head = s;
        f.next = s.next;
        s.next = f;
        ListNode pre;
        while (f.next != null && f.next.next != null) {
            pre = f;
            f = f.next;
            s = f.next;
            f.next = s.next;
            s.next = f;
            pre.next = s;

        }
        return head;
    }

    /**
     * 优化细节后
     *
     * @param head 链表头节点
     * @return 链表头节点
     */
    public ListNode swapPairs_v2(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode f = head;
        ListNode s = head.next;
        if (s != null){
            head = s;
        }
        ListNode pre = new ListNode(0,f);
        while (f != null && s != null) {
            f.next = s.next;
            s.next = f;
            pre.next = s;
            pre = f;
            f = f.next;
            if (f == null){
                s = null;
            }else {
                s = f.next;
            }
        }
        return head;
    }
}
