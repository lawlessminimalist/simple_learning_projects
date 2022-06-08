package Practice_Pair_Coding;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class test {

    //input
    //string []

    //Task: group all anagrams
    //Output: string []

    //example cases:
    // input: ["eat","tea","tan","ate","nat","bat"]
    // every input is valid word, only lowercase
    // output: [["bat"],["nat","tan"],["ate","eat","tea"]]


    // naive solution // 
    // loop through every element
        //check each possible element for an anagram
            //check completed by sorting the word into alphabetical order and comparing

    // O(n^2)

    static void findanagrams(String[] input){
        

        //convert each element into its char array version
        

        List<List<String>> anagrams = new ArrayList<List<String>>();
        HashSet<String> seen = new HashSet<>();

        for(int i = 0;i<input.length;i++){
            String testing_string = input[i];
            char[] testing_char_array = testing_string.toCharArray();

            //create a temporary list
            List<String> temp_list = new ArrayList<String>();
            //add to the list before entering the nested loop
            if(seen.contains(testing_string)){
                continue;
            }
            temp_list.add(testing_string);
            Arrays.sort(testing_char_array);
            seen.add(testing_string);

            //loop through each element and check for anagrams to append
            for(int x = 0;x<input.length;x++){
                //pull and sort the element to test against
                String testing_against = input[x];
                char[] testing_against_char_array = testing_against.toCharArray();
                Arrays.sort(testing_against_char_array);

                if(Arrays.equals(testing_char_array,testing_against_char_array) && !seen.contains(testing_against)){
                    temp_list.add(testing_against);
                    seen.add(testing_against);
                }

            }
            anagrams.add(temp_list);
        }

        System.out.println(anagrams);

    }

    //Room for improvement: convert each element and then grab each matching element from a sorted array/ 

    public static void main(String[] args) {
        String[] input = new String[]{"eat","tea","tan","ate","nat","bat"};
        findanagrams(input);
        System.out.print("Hello");
    }
}
