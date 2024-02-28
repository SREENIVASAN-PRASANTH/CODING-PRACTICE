import java.util.Scanner;


public class swapping_2_numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first Number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        System.out.println("--Before swap--");
        System.out.println("a : " + a);
        System.out.println("b : " + b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("--After swap--");
        System.out.println("a : " + a);
        System.out.println("b : " + b);

    }
}
