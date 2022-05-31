class Solution_Solved {
    public static int[] searchRange(int[] nums, int target) {
        //use binary searcht to locate the first instance of a target element from an array
        //params: 
        // int[] of numbers to search
        // int target number to locate
        //returns:
        //tuple of (index1,index2) or (-1,-1) if not found 

        int left = 0;int right =nums.length-1;
        Integer first=null,last = null;
        //perform binary search
        while(left<=right){
            int m = (left + right)/2;
            if(nums[m]==target){
                first = m;last=m;
                if(m+1 < nums.length && nums[m+1]==target){
                    last = m+1;
                    int index = m+2;
                    while(true){
                        if(index < nums.length && nums[index]==target){
                            last = index;
                            index+=1;
                        }
                        else{break;}
                    }
                }
                if(m-1 >=0 && nums[m-1]==target){
                    first = m-1;
                    int index = m-2;
                    while(true){
                        if(index >=0 && nums[index]==target){
                            first = index;
                            index-=1;
                        }
                        else{break;}
                    }
                }
                return new int[]{first,last};
                
            }
            else if(nums[m]<target){
                left = m+1;
            }
            else if(nums[m]>target){
                right = m-1;
            }
        }

            return new int[]{-1,-1};
        

    }
    public static void main(String[] args) {
        int[] nums = {3,3,3,3,3};
        int target = 3;
        int[] x = searchRange(nums,target);
        System.out.println(x);
    }
}