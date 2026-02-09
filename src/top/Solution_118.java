package top;

import java.util.ArrayList;
import java.util.List;

/**
 * <a href="https://leetcode.cn/problems/pascals-triangle/?envType=study-plan-v2&envId=top-100-liked">118. 杨辉三角</a>
 * <p>
 * <p>
 * <p>
 * 1 <= numRows <= 30
 *
 * <p>
 * <p>
 *
 * @author schne
 * @since 2026/1/14
 */
public class Solution_118 {

    public List<List<Integer>> generate(int numRows) {
        ArrayList<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> first = new ArrayList<>();
        first.add(1);
        result.add(first);
        for (int row = 1; row < numRows; row++) {
            ArrayList<Integer> rowList = new ArrayList<>(row + 1);
            rowList.add(1);
            List<Integer> befor = result.getLast();
            for (int i = 1; i < row; i++) {
                rowList.add(befor.get(i - 1) + befor.get(i));
            }
            rowList.add(1);
            result.add(rowList);
        }
        return result;
    }
}
