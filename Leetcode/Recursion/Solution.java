
public class Solution {
    public static void ReverseString(char[] s) {
        System.out.println(helper(s, 0));
    }

    public static char[] helper(char[] s,int index){
        if(index>=s.length/2){
            return s;
        }
        int p2 = (s.length-1)-index;
        char temp = s[index];
        s[index] = s[p2];
        s[p2] = temp;
        return helper(s,index+1);

    }
    public static void main(String[] args) {
        char[] s = {'h','e','l','l','o'};
        Solution.ReverseString(s);
    }
}
