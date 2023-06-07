/**
 * Removes duplicates of sorted input array
 * @param {number[]} nums input of sorted numbers
 * @returns {number[]} array of unique elements in nums
 */
var removeDuplicates = function(nums) {
    let i = 0, j = 0;
    while (j < nums.length) {
        if (nums[j] !== nums[i]) {
            i += 1;
            nums[i] = nums[j];
        } j += 1
    } return nums.slice(0, i + 1);
    // return nums.slice(0, i + 1).length
}