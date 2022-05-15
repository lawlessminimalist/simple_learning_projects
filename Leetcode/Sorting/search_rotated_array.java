import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public static int search(int[] nums, int target) {
        HashMap<Integer,Integer> index = new HashMap<Integer,Integer>();
        for(int i = 0;i<nums.length;i++){
            //record the indexes of the orginial array
            index.put(nums[i], i);
        }
        
        //sort the array to perform a binary search
        Arrays.sort(nums);
        int l = 0;int r = nums.length-1;
        while(l<=r){
            int m = (l+ r) /2;
            if (nums[m] == target){
                return index.get(nums[m]);
            }
            if(nums[m]<target){
                l = m+1;
            }
            else if(nums[m]>target){
                r = m-1;
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        int[] nums = new int[]{1};int target = 2;
        System.out.println(search(nums,target));
    }
}