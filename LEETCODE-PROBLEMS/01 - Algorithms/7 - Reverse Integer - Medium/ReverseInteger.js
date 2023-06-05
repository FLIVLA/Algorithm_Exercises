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

/**
 * Time Complexity: Linear | O(n) where n is the number of digits in x
 * @param {*} x input integer
 * @returns reversed digits as integer
 */
var reverseInt = function(x) {
    if (x === 0) {
        return x;
    } else if (x < 0) {
        let revStr = ""
        for (let i = Math.abs(x).toString().length - 1; i >= 0; i--) {
            revStr += Math.abs(x).toString()[i];
        }
        let res = parseInt(revStr) * -1;
        if (res >= -Math.pow(2, 31)) {
            return res;
        } else return 0;
    } else {
        let xStr = x.toString(), revStr = "";
        for (let i = xStr.length - 1; i >= 0; i--) {
            revStr += xStr[i];
        }
        let num = parseInt(revStr);
        if (num <= Math.pow(2, 31) - 1) {
            return num;
        } else return 0;
    }
}