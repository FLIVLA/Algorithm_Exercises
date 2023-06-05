/*
 * You are given a large integer represented as an integer 
 * array digits, where each digits[i] is the ith digit of the integer. 
 * The digits are ordered from most significant to least significant 
 * in left-to-right order. The large integer does not contain any leading 0's. 
 * 
 * Increment the large integer by one and return the resulting array of digits.
 */

import java.util.Arrays;

public class PlusOne {
    
    public int[] plusOne_1(int[] digits) {
        digits[digits.length - 1] += 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            if (i > 0) {
                if (digits[i] == 10) {
                    digits[i] = 0;
                    digits[i - 1] += 1;
                } else break;           // BREAK! decreases runtime significantly
            } else {
                if (digits[i] == 10) {
                    digits[i] = 1;
                    int[] res = Arrays.copyOf(digits, digits.length + 1);
                    res[res.length - 1] = 0;
                    return res;
                }
            }
        } return digits;
    }
}
