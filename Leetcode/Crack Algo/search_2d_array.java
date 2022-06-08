class Solution {
    public static boolean searchMatrix(int[][] matrix, int target) {
        //iterate through each row to determine the search space
        boolean result = false;
        for(int[] row:matrix){
            if(row[row.length-1]>=target){
                //perform binary search on the row to find the target
                 result = binarysearch(row, target);
                 break;
            }
        }
        return result;
    }

    private static boolean binarysearch(int[] row, int target){
        int left = 0;int right = row.length-1;
        while(left<=right){
            int m = (left + right)/2;
            
            if(row[m] == target){
                return true;
            }
            if(row[m]<target){
                left = m+1;

            }
            else if(row[m]>target){
                right = m-1;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[][] matrix = new int[][]{{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        int[][] matrix_ez = new int[][]{{1}};

        int target = 1;
        System.out.print(searchMatrix(matrix, target));
    }
}