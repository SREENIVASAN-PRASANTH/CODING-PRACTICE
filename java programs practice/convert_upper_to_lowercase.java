import java.util.Scanner;
public class convert_upper_to_lowercase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String str1 = sc.nextLine();

        String result = "";

        for (int i = 0;i < str1.length();i ++){
            result += Character.toLowerCase(str1.charAt(i));
        }

        System.out.println("The lower case converted string = " + result);

        String result2 = "";

        for (int i = 0; i < str1.length();i ++){
            result2 += Character.toUpperCase(result.charAt(i));
        }

        System.out.println("The upper converted String is = " + result2);
    }
}
