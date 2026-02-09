package top;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * <a href="https://leetcode.cn/problems/word-break/?envType=study-plan-v2&envId=top-100-liked">139. 单词拆分</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *   唉~ 实在不行就暴力解  至少不会错
 *
 * @author schne
 * @since 2026/1/12
 */
public class Solution_139 {



    public static void main(String[] args) {
//        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        ArrayList<String> list = new ArrayList<>();
        list.add("a");
        list.add("aa");
        list.add("aaa");
        list.add("aaaa");
        list.add("aaaaa");
        list.add("aaaaaa");
        list.add("aaaaaaa");
        list.add("aaaaaaaa");
        list.add("aaaaaaaaa");
        list.add("aaaaaaaaaa");
        boolean leetcode = new Solution_139().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", list);
//       list.add("b");
//       list.add("bb");
//        boolean leetcode = new Solution_139().wordBreak("bbb", list);
        System.out.println(leetcode);
    }

    public static int[][] dp;

    public boolean wordBreak(String s, List<String> wordDict) {
        List<Word> intervals = new ArrayList<>();
        for (String word : wordDict) {
            List<Integer> list = kmp(s, word);
            for (Integer i : list) {
                intervals.add(new Word(i, word.length()));
            }

        }
        intervals.sort((o1, o2) -> Objects.equals(o1.index, o2.index) ? o1.length - o2.length : o1.index - o2.index);
        dp = new int[s.length()+1][intervals.size()+1];
        boolean f = f(0, s.length(), 0, intervals);
        return f;
    }

    private List<Integer> kmp(String s, String subStr) {
        List<Integer> list = new ArrayList<>();
        if (s.isEmpty()) {
            return list;
        }
        char[] charArray = s.toCharArray();
        char[] subStrCharArray = subStr.toCharArray();
        int[] next = nextArray(subStrCharArray);
        int m = s.length();
        int n = subStr.length();
        int x = 0, y = 0;
        while (x < m) {
            if (charArray[x] == subStrCharArray[y]) {
                x++;
                y++;
            } else if (y == 0) {
                x++;
            } else {
                y = next[y];
            }
            if (y == n) {
                list.add(x - y);
                x = x - y + 1;
                y = 0;
            }
        }
        return list;
    }

    private int[] nextArray(char[] chars) {
        if (chars.length == 1) {
            return new int[]{-1};
        }
        int[] next = new int[chars.length];
        next[0] = -1;
        next[1] = 0;
        int i = 2;
        int cn = 0;
        while (i < next.length) {
            if (chars[i - 1] == chars[cn]) {
                next[i++] = ++cn;
            } else if (cn > 0) {
                cn = next[cn];
            } else {
                next[i++] = 0;
            }
        }
        return next;
    }

    // TODO 后面再看下这个改写动态规划
    private boolean f(int start, int l, int index, List<Word> list) {
        if (dp[start][index] != 0) {
            return dp[start][index] > 0;
        }
        if (start == l) {
            dp[start][index] = 1;
            return true;
        }
        if (index == list.size()) {
            dp[start][index] = -1;
            return false;
        }
        Word word = list.get(index);
        if (word.index > start) {
            dp[start][index] = -1;
            return false;
        }
        if (word.index < start) {
            boolean f = f(start, l, index + 1, list);
            dp[start][index] = f ? 1: -1;
            return f;
        }
        boolean b = f(start, l, index + 1, list) || f(start + word.length, l, index + 1, list);
        dp[start][index] = b ? 1: -1;
        return b;
    }

    public void build(int start, int l, int index, List<Word> list){
        int j= 0,i =0;
        dp[i][j] =   (dp[i][j+1] > 0 ||  dp[i+list.get(j).length][j+1] > 0) ? 1 :-1;
    }

}

class Word {
    int index;
    int length;

    public Word(int index, int length) {
        this.index = index;
        this.length = length;
    }
}