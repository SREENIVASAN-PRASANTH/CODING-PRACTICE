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
    }
}
