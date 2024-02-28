import java.util.Scanner;

public class greatest_of_3_no {
    public static void main(String[] args) {
        int a,b,c,largest,temp;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: ");
        a = sc.nextInt();
        System.out.println("Enter the secind number: ");
        b = sc.nextInt();
        System.out.println("Enter the third number: ");
        c = sc.nextInt();
        temp = a > b?a : b;
        largest = c > temp ? c : temp;
        System.out.println("The largest Number is: " + largest);
    }
}
