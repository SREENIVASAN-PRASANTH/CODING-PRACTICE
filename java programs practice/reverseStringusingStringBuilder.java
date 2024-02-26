import java.util.Scanner;

public class reverseStringusingStringBuilder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String : ");
        String String = sc.nextLine();
        StringBuilder str = new StringBuilder(String);
        System.out.println("String = " + str.toString());
        
        StringBuilder reverseStr = str.reverse();
        System.out.println("Reversed String = " + reverseStr.toString());
    }
}
