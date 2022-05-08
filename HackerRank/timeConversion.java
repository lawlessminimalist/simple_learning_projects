package HackerRank;
public class timeConversion {
    public static void main(String[] args) {
        String s = "07:05:45PM";
        System.out.println(timeconversion(s));

    }

    public static String timeconversion(String s) {
            String pm_test = "PM";
            Boolean pm = s.contains(pm_test);
            if(pm){
                int converter = Integer.parseInt(s.substring(0, 2));
                converter +=10;
                String new_hour = String.valueOf(converter);
                s = new_hour + s.substring(2,s.length());
                s = s.substring(0, s.length()-2);
            }
            else{
                s = s.substring(0, s.length()-2);
            }
            return s;

        }
}
