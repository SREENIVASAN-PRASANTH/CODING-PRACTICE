import java.util.Scanner;

public class oddeven {
    public static void main(String[] args) {
        int num;
        System.out.println("Enter a number");
        Scanner s = new Scanner(System.in);
        num = s.nextInt();

        if (num % 2 == 0){
            System.out.println("It is a even number");
        }
        else{
            System.out.println("It is a odd number");
        }

    }
}
