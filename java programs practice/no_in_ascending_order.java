import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class no_in_ascending_order {
    public static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the number of inputs:");
        int num1 = Integer.parseInt(in.readLine());
        int[] arr = new int[num1];

        for (int i = 0; i < num1;i ++){
            System.out.println("Enter the value #" + (i + 1) + ":");
            arr[i] = Integer.parseInt(in.readLine());

        }

        Arrays.sort(arr);
        System.out.println("Numbers in descending order: ");
        for(int i = 0 ;i <arr.length;i++){
            System.out.print(" " + arr[i]);
        }
    }
}

