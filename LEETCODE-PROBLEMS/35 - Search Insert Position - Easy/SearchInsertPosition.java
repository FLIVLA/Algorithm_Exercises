/**
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

------------------------------------------------------------------
 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

-------------------------------------------------------------------
Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4

 */
public class SearchInsertPosition {

    /**
     * Using binary search is the efficient way of solving the problem
     * Time Complexity: Logarithmic | O(log n) where n is the length of nums
     * @param nums input sorted array of integers
     * @param t target value
     * @return index of t in nums
     */
    public int searchInsertPos(int[] nums, int t) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l + 1) / 2;
            if (nums[m] < t) {
                l = m + 1;
            } else if (nums[m] > t) {
                r = m - 1;
            } else return m;
        } return l;
    }
}
