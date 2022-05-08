
import java.util.*;


class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        float length = arr.size();
        int pos = 0;int neg = 0;int neut=0;
        for(int i : arr){
            if(i > 0){pos+=1;}
            if(i < 0){neg+=1;}
            if(i == 0){neut+=1;}
        }
        System.out.printf("%.6f", pos/length);
        System.out.println("");

        System.out.printf("%.6f", neg/length);
        System.out.println("");

        System.out.printf("%.6f", neut/length);

    }

    public static void main(String[] args) {
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        arr.add(2);
        arr.add(3);
        plusMinus(arr);
    }

}
