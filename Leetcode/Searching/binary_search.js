/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
        //define the variables that maintain the search interval
        let low = 0,high = nums.length-1;
        //enter into a loop that searches until finding target or empties the search interval
        //low <= high as we need to check the actual values of each of these vars
        while(low<=high){
            //known bug with mid = low + high / 2, will cause an overflow
            let mid = Math.floor(low + ((high - low) / 2));
            if(nums[mid] == target){
                return mid;
            }
            //add or subtract one to move the search space out of the known false mid index
            else if(nums[mid]< target){
                low = mid+1;
            }
            else if(nums[mid] > target){
                high = mid-1;
            }
        }
        //if not found return -1
        return -1;        
            
};




let nums = [5]
let target = 5

console.log(search(nums,target))