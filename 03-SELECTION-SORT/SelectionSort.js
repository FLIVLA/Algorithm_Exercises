var selectionSort = function(nums) {
    let n = nums.length;
    for (let i = 0; i < n; i++) {
        var min = i;
        for (let j = i + 1; j < n; j++) {
            if (nums[j] < nums[min]) min = j
        } 
        // do the exchange
        let t = nums[i]; 
        nums[i] = nums[j]; 
        nums[j] = t;
    } return nums; // return sorted
}