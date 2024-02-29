import java.io.*;
import java.util.Scanner;
class sub_adjacent_digits{
    static int RSF(int n){
        while(n >= 10){
            int x = n;
            int l = 0;
            while(n >0){
                n = n/10;
                l++;
            }
            int a[] = new int[l];
            int i = l - 1;
            while (x > 0){
                a[i] = x % 10;
                x = x/10;
                i--;
            }
            for(int j = 0;j < l-1;j ++){
                n = n * 10+ Math.abs(a[j] - a[j+1]);
            }
        }
        return n;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = sc.nextInt();
        int ans = RSF(n);
        System.out.println("The answer is: " + ans);
    }
}