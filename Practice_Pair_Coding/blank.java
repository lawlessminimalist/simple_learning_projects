import java.util.Arrays;

class Solution{

    /*
    brief
    kth largest element in an array
    ex. 
    input
    [3,2,1,5,6,4]
    [3,2,3,1,2,4,5,5,6]
    k=2
    k=4
    output
    5
    index = 3
    4
    */


    // naive solution
    // sort the array in place in reverse order
    // iterate through the array until kth element


    //hashmap of encoutered element 





    public static void main(String[] args) {
        int[] input = new int[]{3,2,3,1,2,4,5,5,6};
        int k = 4;
        int result = findKthElement(input,k);
        System.out.print(result);
    }


    static int findKthElement(int[] input, int k){

        Arrays.sort(input);
        return input [input.length-k];

    }




}