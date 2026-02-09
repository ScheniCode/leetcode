package top;

import java.util.HashMap;
import java.util.Map;

/**
 * <a href="https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked">138. 随机链表的复制</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 思路比较简单
 * 两次遍历
 * 第一次复制val和next,新链表的random仍然指向旧链表的对应节点并把新旧节点的映射关系存入map
 * 第二次遍历根据映射关系设置random
 *
 * @author schnei
 * @since 2026/1/20
 */
public class Solution_138 {

    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Node index = head.next;
        Node cur;
        Node copy = new Node(head.val);
        Node pre = copy;
        copy.random = head.random;
        Map<Node, Node> map = new HashMap<>();
        map.put(head, copy);
        while (index != null) {
            cur = new Node(index.val);
            cur.random = index.random;
            pre.next = cur;
            map.put(index, cur);
            index = index.next;
            pre = cur;
        }
        index = copy;
        while (index != null) {
            index.random = map.get(index.random);
            index = index.next;
        }
        return copy;
    }
}

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
