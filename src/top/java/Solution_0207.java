package top.java;

import java.util.*;

/**
 * <a href="https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked">207. 课程表</a>
 * <p>
 * <p>
 * 暴力解 构建所有节点的父子关系  从无前置课程的课程号开始逐步释放   最后判断集合中还有没有元素
 * <p>
 * <p>
 * 最优解：邻接表/链式前向星建图
 * 同时维护每个点的入度
 * 入度为零的点丢入队列遍历
 * 依次维护对应子节点的入度
 * 有减到0的节点再丢到队列中去
 * 最终判断邻接表中还有没有节点
 * <p>
 * 如果是有向无环图则可以全部学完
 *
 * @author schnei
 * @since 2026/2/16
 */
public class Solution_0207 {

    public static void main(String[] args) {
        int[][] prerequisites = new int[4][2];
        prerequisites[0][0] = 1;
        prerequisites[0][1] = 4;

        prerequisites[1][0] = 2;
        prerequisites[1][1] = 4;

        prerequisites[2][0] = 3;
        prerequisites[2][1] = 1;

        prerequisites[3][0] = 3;
        prerequisites[3][1] = 2;

        System.out.println(new Solution_0207().canFinish(5, prerequisites));
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        HashMap<Integer, List<Integer>> leaf = new HashMap<>();
        HashMap<Integer, List<Integer>> parent = new HashMap<>();
        int[] ints = new int[numCourses];
        for (int[] point : prerequisites) {
            List<Integer> l = leaf.get(point[1]);
            if (l == null) {
                l = new ArrayList<>();
                leaf.put(point[1], l);
            }
            l.add(point[0]);

            List<Integer> p = parent.get(point[0]);
            if (p == null) {
                p = new ArrayList<>();
                parent.put(point[0], p);
            }
            p.add(point[1]);
            ints[point[0]] = 1;
        }
        Queue<Integer> zero = new PriorityQueue<>();
        Queue<Integer> one = new PriorityQueue<>();
        for (int i = 0; i < numCourses; i++) {
            if (ints[i] == 0) {
                zero.add(i);
            } else {
                one.add(i);
            }
        }

        while (!zero.isEmpty()) {
            int i = zero.poll();
            List<Integer> leafList = leaf.get(i);
            if (leafList != null) {
                for (Integer j : leafList) {
                    List<Integer> parentList = parent.get(j);
                    parentList.removeIf(el -> el.equals(i));
                    if (parentList.isEmpty()) {
                        parent.remove(j);
                        one.remove(j);
                        zero.add(j);
                    }
                }
                leaf.remove(i);
            }
        }
        return one.isEmpty();

    }
}
