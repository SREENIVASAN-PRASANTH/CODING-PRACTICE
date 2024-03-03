import java.util.*;
public class string_to_integer {

    public static int convertNumber(String str){
        int val = 0;
        System.out.println("String =" + str);
        try{
            val = Integer.parseInt(str);
        }
        catch (NumberFormatException e){
            System.out.println("Invalid String");
        }
        return val;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        String str = sc.nextLine();
        int val = convertNumber(str);
        System.out.println("Number = " + val);

        String str2 = "1234";
        System.out.println("String2 = " + str2);
        int val2 = Integer.valueOf(str2);
        System.out.println("Number2 = " + val2);
    }
}
