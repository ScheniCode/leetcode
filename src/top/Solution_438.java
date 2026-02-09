package top;

import java.util.*;

/**
 * <a href="https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked">438. 找到字符串中所有字母异位词</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 * 我的方法实际上是暴力解
 * <p>
 * 最优解：先统计词频存入int[] ch = new int[26]; 右边界从0开始遍历，从ch减去对应的词频，
 * 当右边界对应位置词频小于0时左边界右移动直到右边界对应词频不小于0，如果长度刚好等于p则记录左边界下标
 *
 * @author schnei
 * @since 2026/1/23
 */
public class Solution_438 {

    public static void main(String[] args) {
        List<Integer> list = new Solution_438().findAnagrams("abab", "ab");
        System.out.println(list);
    }

    // 试试滑动窗口

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) {
            return result;
        }
        // p的词频
        Map<String, Integer> map = new HashMap<>();
        for (char c : p.toCharArray()) {
            map.put(String.valueOf(c), map.getOrDefault(String.valueOf(c), 0) + 1);
        }
        Map<String, Integer> window = new HashMap<>();
        char[] charArray = s.toCharArray();
        for (int i = 0; i < p.length(); i++) {
            window.put(String.valueOf(charArray[i]), window.getOrDefault(String.valueOf(charArray[i]), 0) + 1);
        }
        int start = 0;
        int end = p.length() - 1;
        if (check(map, window)) {
            result.add(start);
        }
        while (end < s.length() - 1) {
            Integer count = window.get(String.valueOf(charArray[start]));
            if (count == 1) {
                window.remove(String.valueOf(charArray[start]));
            } else {
                window.put(String.valueOf(charArray[start]), count - 1);
            }
            window.put(String.valueOf(charArray[end + 1]), window.getOrDefault(String.valueOf(charArray[end + 1]), 0) + 1);
            start++;
            end++;
            if (check(map, window)) {
                result.add(start);
            }
        }
        return result;
    }

    private boolean check(Map<String, Integer> map, Map<String, Integer> window) {
        if (map.size() != window.size()) {
            return false;
        }
        Set<String> keySet = map.keySet();
        Optional<String> first = keySet.stream().filter(key -> !Objects.equals(map.get(key), window.get(key))).findFirst();
        return first.isEmpty();
    }
}
