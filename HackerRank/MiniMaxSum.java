package HackerRank;
import java.util.*;
class Result {

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        arr.sort(Comparator.naturalOrder());
        var max = arr.subList(arr.size()-4, arr.size());
        var min = arr.subList(0, 4);

        double[] new_max = max.stream().mapToDouble(i -> (double)i).toArray();
        double[] new_min = min.stream().mapToDouble(i -> (double)i).toArray();

        double res_min = Arrays.stream(new_min).sum();
        double res_max = Arrays.stream(new_max).sum();

        System.out.printf("%.0f %.0f",res_min,res_max);
    }

    public static void main(String[] args) {
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(256741038);
        arr.add(623958417);
        arr.add(467905213);
        arr.add(714532089);
        arr.add(938071625);
        miniMaxSum(arr);
    }

}

    
