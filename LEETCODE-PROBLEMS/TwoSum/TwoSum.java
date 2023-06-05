import java.util.HashMap;

// NOTE: this was translated from the python version.

/*
 * Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target. 
 * You may assume that each input would have exactly one solution, 
 * and you may not use the same element twice. 
 * You can return the answer in any order.
 */

public class TwoSum {

    /** O(n^2) - Quadratic
     * The not so efficient O(n^2) approach.
     * @param nums input array of integers
     * @param t Target value of the two integers added
     * @return indexes of two integers that sums to target
     */
    public int[] twoSum_1(int[] nums, int t) {
        for (int i = 0; i < nums.length; i++) {
            int j = nums.length - 1;
            while (j > i) {
                if (nums[i] + nums[j] == t) {
                    return new int[]{i, j};
                } else j--;
            }
        } return new int[]{};
    }


    /** O(n) - Linear
     * This approach is optimal for the twoSum problem, 
     * as we solve it with O(n), single loop over the input array. 
     * the for loope iterates over the array of integers and 
     * uses enumerate to get both index and number of current iteration. 
     * In each iteration c = t - num is calculated and if c exist in 
     * the hashtable, we return [hashtable[c], i]. if not, num is 
     * added to the hashtable with index i. 
     * @param nums input array of integers
     * @param t Target value of the two integers added
     * @return indexes of two integers that sums to target
     */
    public int[] twoSum_2(int[] nums, int t) {
        HashMap<Integer, Integer> idxMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int c = t - nums[i];
            if (idxMap.get(c) != null) {
                return new int[]{idxMap.get(c), i};
            } idxMap.put(nums[i], i);
        } return new int[]{};
    }
}
