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

class ReverseInt {

    /**
     * Time Complexity: Linear | O(n) where n is the number of digits in x
     * @param x input integer
     * @returns reversed digits as integer
     */
    public reverseInt(x: number): number {
        if (x === 0) return x;
        else {
            let revStr: string = "", xAbsStr: string = Math.abs(x).toString();
            for (let i = xAbsStr.length - 1; i >= 0; i--) {
                revStr += xAbsStr[i];
            }
            if (x < 0) revStr = "-" + revStr;
            let num = parseInt(revStr);
            if (num >= -Math.pow(2, 31) && num <= Math.pow(2, 31) - 1) return num;
            else return 0;
        }
    }
}