/*
 * Given a string s, find the length of the longest
 * substring without repeating characters.
 * 
 * Constraints:
 *  - 0 <= s.length <= 5 * 10^4
 *  - s consists of English letters, digits, symbols and spaces.
 */

import java.util.HashSet;
import java.util.Set;

public class LongestSub {

    /** Time complexity of the algorithm: O(n) - n is the length of the input string
     * Finds the length of the longest substring without repeating characters.     
     * @param s the input string
     * @return the length of the longest substring without repeating characters
     */
    public int longestSub(String s) {
        // pointers
        int l = 0;
        int r = -1;
    
        char[] sar = s.toCharArray();
        int max = 0;
        Set<Character> sub = new HashSet<>();
        while (r < sar.length - 1) {
            if (!sub.contains(sar[r + 1])) {
                sub.add(sar[r + 1]);
                r += 1;
                max = Math.max(max, r - l + 1);
            } else {
                sub.remove(sar[l]);
                l += 1;
            }
        } return max;
    }
}
