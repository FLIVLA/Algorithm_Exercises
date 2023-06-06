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

/**
 * Time Complexity: O(n) where n is length of s
 * @param {*} s input string
 * @param {*} n number of rows
 * @returns converted zigzag string
 */
var zigZagConversion = function(s, n) {
    if (n >= s.length || n <= 1) {
        return s;
    } else {
        let rows = [...Array].fill("");  // Initialize new array with n empty strings
        let idx = 0, step = 1;
        for (const c of s) {
            rows[idx] += c;
            if (idx == 0) {
                step = 1;
            } else if (idx == n - 1) {
                step = -1;
            } idx += step;
        } return rows.join("");
    }
}