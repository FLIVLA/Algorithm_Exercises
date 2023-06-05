/**
 * Given a signed 32-bit integer x, return x with its digits reversed. 
 * If reversing x causes the value to go outside the signed 32-bit 
 * integer range [-231, 231 - 1], then return 0.
 * 
 * Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 * 
 * Example 1:
 * - Input: x = 123
 * - Output: 321
 */

public class ReverseInteger {
    
    /**
     * Time Complexity: Linear | O(n) where n is the number of digits in x
     * @param x input integer
     * @return reversed digits as integer
     */
    public int reverseInt(int x) {
        if (x == 0) {
            return x;
        } else {
            String revStr = "";
            char[] xArr = String.valueOf(Math.abs(x)).toCharArray();
            for (int i = xArr.length - 1; i >= 0; i--) {
                revStr += xArr[i];
            }
            if (x < 0) revStr = "-" + revStr; // Add the "-" sign back to string
            try {
                long y = Long.parseLong(revStr);
                if (y >= Integer.MIN_VALUE && y <= Integer.MAX_VALUE) return (int) y;
                else return 0;
            } catch (NumberFormatException e) { return 0; }
        }
    }
}
