package top;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * <a href="https://leetcode.cn/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked">23. 合并 K 个升序链表</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 我的思路：每个链表的头节点放到一个小根堆里，取出最小的节点，并把这个节点的下一个节点放入堆，链表总数多了之后会影响堆调整的开销
 * <p>
 * 最优解：两个一组合并，使得链表总数减半，然后再重复执行上诉步骤，直到只剩一个链表
 *
 * @author schnei
 * @since 2026/1/14
 */
public class Solution_23 {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> queue = new PriorityQueue<>(Comparator.comparingInt(node -> node.val));
        for (ListNode node : lists) {
            if (node != null) {
                queue.add(node);
            }
        }
        ListNode h = null;
        ListNode t = null;
        while (!queue.isEmpty()) {
            ListNode first = queue.poll();
            if (first.next != null) {
                queue.add(first.next);
            }
            if (h == null) {
                h = first;
            }
            if (t != null) {
                t.next = first;
            }
            t = first;

        }
        return h;
    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
