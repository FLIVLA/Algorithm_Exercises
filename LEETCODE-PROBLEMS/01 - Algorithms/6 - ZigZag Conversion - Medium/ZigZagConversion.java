/*
 * The string "PAYPALISHIRING" is written in a zigzag pattern on 
 * a given number of rows like this: 
 * (you may want to display this pattern in a fixed font for better legibility)
 * 
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * 
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion given a number of rows:
 * 
 * string convert(string s, int numRows);
 * Example 1:
 * - Input: s = "PAYPALISHIRING", numRows = 3
 * - Output: "PAHNAPLSIIGYIR"
 */

import java.util.Arrays;
public class ZigZagConversion {

    /**
     * Time Complexity: O(n) where n is length of s
     * @param s input string
     * @param n number of rows
     * @return converted zigzag string
     */
    public String zigZag_Convert(String s, int n) {
        if (n >= s.length() || n <= 1) {
            return s;
        } else {
            String[] rows = new String[n];
            Arrays.fill(rows, "");
            int idx = 0;
            int step = 1;
            char[] sar = s.toCharArray();
            for (char c : sar) {
                rows[idx] += c;
                if (idx == 0) {
                    step = 1;
                } else if (idx == n - 1) {
                    step = -1;
                }
                idx += step;
            }
            return String.join("", rows);
        }
    }
}
