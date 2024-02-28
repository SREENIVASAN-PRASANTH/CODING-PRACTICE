import java.util.Scanner;
public class odd_no_count {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the range: ");
        int number = sc.nextInt();
        System.out.print("List of odd numbers from 1 to " + number + ": ");
        for (int i = 1;i<=number;i++){
            if(i % 2 !=0){
                System.out.print(i + " ");
            }
        }
    }
}
