class BinarySearch {
    /**
     * BINARY SEARCH FOR SORTED NUMBER[]
     * Time Complexity: Linear | O(log n)
     * @param nums input sorted number array
     * @param t target value
     * @returns index of t in nums
     */
    public search_PosOf_t(nums: number[], t: number): number {
        var l = 0, r = nums.length - 1;
        while (l <= r) {
            var m = Math.floor((l + r) / 2);
            if (nums[m] < t) {
                l = m + 1;
            } else if (nums[m] > t) {
                r = m - 1;
            } else return m;
        } return l;
    }
}