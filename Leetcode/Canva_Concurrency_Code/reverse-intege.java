class Soltuion_wk2_1{
    public static void main(String[] args){
        int x = -1534236469;
        System.out.println(reverseIntegerString(x));

        System.out.println(Integer.MAX_VALUE);
        System.out.println(x*10 > (double)Integer.MAX_VALUE);



    }


    //first int reversal algo
    public static int reverseIntegerMath(int x){
        //detect if reversing the int will cause an overflow
        long reverse= 0;
        boolean neg = x > 0? false:true;
        if(neg)x*=-1;
        while(x>0){
            //check if num negative
            if(x > 0){}
            int lastdigit = x % 10;
            //checking for overflow using overhead of long type
            long test = (reverse * 10) + lastdigit;
            if (test > Integer.MAX_VALUE){
                return 0;
            }
            reverse = (reverse * 10) + lastdigit;
            x = x / 10 ;
        }
        if(neg)reverse*=-1;
        return (int)reverse;
    }

    public static int reverseIntegerString(int x){
        String target = Integer.toString(x);
        boolean isNeg = false;
        if(target.charAt(0)== '-'){
            target = target.substring(1);
            isNeg = true;
        }
        int pointerb = target.length()-1;
        char[] arr = target.toCharArray();

        for(int pointera = 0; pointera<target.length()/2;pointera++){ 
            char temp = arr[pointera];
            arr[pointera]= arr[pointerb];
            arr[pointerb] = temp;
            pointerb--;
        }
        target = String.valueOf(arr);
        double test = Double.parseDouble(target);
        if(test > Integer.MAX_VALUE){
            return 0;
        }
        if(isNeg){
            test = test*-1;
        }
        return (int)test;
    }




}