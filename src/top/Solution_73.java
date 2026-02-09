package top;

import java.util.ArrayList;

/**
 * <a href="https://leetcode.cn/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-100-liked">73. 矩阵置零</a>
 * <p>
 * <p>
 *
 * <p>
 * <p>
 *
 * @author schnei
 * @since 2026/1/16
 */
public class Solution_73 {

    /**
     * 暴力解先走一个
     *
     * @param matrix 入参矩阵
     */
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        ArrayList<int[]> list = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0){
                    int[] point = new int[2];
                    point[0] = i;
                    point[1] = j;
                    list.add(point);
                }
            }
        }
        for (int[] ints : list) {
            for (int i = 0; i <n; i++) {
                matrix[ints[0]][i] = 0;
            }
            for (int i = 0; i < m; i++) {
                matrix[i][ints[1]] = 0;
            }
        }
    }
}
