package algo_timing;
class Soltuion_wk2_1{


    public static long startTime = System.currentTimeMillis();

    public static long endTimeStringMethod = 0;
    public static long endTimeMathMethod = 0;
    public static void main(String[] args){

     // Create two threads:
        Thread thread1 = new Thread(){
            public void run() {
                for(int x = 0;x<9999999*10;x++){
                    reverseIntegerMath(x);
                }
                endTimeMathMethod = System.currentTimeMillis();

        };
    };
        Thread thread2 = new Thread(){
            public void run() {
                for(int x = 0;x<9999999*10;x++){
                    reverseIntegerString(x);
                }
                endTimeStringMethod = System.currentTimeMillis();
            }
        };

                // Start the downloads.
        thread1.start();
        thread2.start();

        try{
                    // Wait for them both to finish
        thread1.join();
        thread2.join();
        }
        catch(Exception e){
            System.out.print(e.getMessage());
        }
        System.out.println("Total execution time for string method: " + (double)(endTimeStringMethod - startTime));
        System.out.println("Total execution time for math method: " + (double)(endTimeMathMethod - startTime));




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