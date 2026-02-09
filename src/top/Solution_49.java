package top;

import java.util.*;

/**
 * <a href="https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked">49. 字母异位词分组</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *     简单粗暴，每个字符串重新排序后分组
 *
 * @author schnei
 * @since 2026/1/16
 */
public class Solution_49 {
    /**
     * 唉~ 上来只能想到暴力解
     *
     * @param strs
     * @return
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            String s = sort(str);
            if (!map.containsKey(s)){
                map.put(s,new ArrayList<>());
            }
            map.get(s).add(str);
        }
        return new ArrayList<>(map.values());
    }

    public String sort(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        char[] charArray = str.toCharArray();
        Arrays.sort(charArray);
        return String.valueOf(charArray);
    }
}
