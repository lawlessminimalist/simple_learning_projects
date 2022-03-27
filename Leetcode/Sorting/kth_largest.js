var findKthLargest = function(nums, k) {
    nums.sort().reverse();
    return nums[k-1];

}

let nums = [-1,-1];
let k = 2;
console.log(findKthLargest(nums,k));

