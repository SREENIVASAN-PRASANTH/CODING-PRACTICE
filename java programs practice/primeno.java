import java.util.Scanner;

class primeno{
    public static void main(String[] args) {
        int n,i,s=0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        
        if (n > 1){
            for(i = 1;i <= n;i ++){
                if (n % i == 0){
                    s++;
                }
            }
            if(s == 2){
                System.out.println(n+":Prime");
            }
            else{
                System.out.println(n+":Composite");
            }
        }
        else{
            System.out.println(n+":Invalid");
        }
    }
}