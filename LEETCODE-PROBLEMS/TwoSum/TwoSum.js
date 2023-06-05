/** O(n^2) - Quadratic
 * The not so efficient O(n^2) approach.
 * @param {*} nums input array of integers
 * @param {*} t Target value of the two integers added
 * @returns indexes of two integers that sums to target
 */
var twoSum_1 = function(nums, t) {
    for (let i = 0; i < nums.length; i++) {
        j = nums.length - 1;
        while (j > i) {
            if (nums[i] + nums[j] === t) {
                return [i, j];
            } else j--;
        }
    } return []
};

/** O(n) - Linear
 * This approach is optimal for the twoSum problem, 
 * as we solve it with O(n), single loop over the input array. 
 * the for loope iterates over the array of integers and 
 * uses enumerate to get both index and number of current iteration. 
 * In each iteration c = t - num is calculated and if c exist in 
 * the hashtable, we return [hashtable[c], i]. if not, num is 
 * added to the hashtable with index i. 
 * @param {*} nums input array of integers
 * @param {*} t Target value of the two integers added
 * @returns indexes of two integers that sums to target
 */
var twoSum_2 = function(nums, t) {
    let idxMap = {};
    for (let i = 0; i < nums.length; i++) {
        let c = t - nums[i];
        if (idxMap[c] !== undefined) {
            return [idxMap[c], i];
        } else idxMap[nums[i]] = i;
    } return [];
};