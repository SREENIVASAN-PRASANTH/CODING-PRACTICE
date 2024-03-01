import java.util.Scanner;
public class matrix_multiplication{

    static int[][] getMatrix(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the no of rows of matrix: ");
        int row = sc.nextInt();
        System.out.print("Enter the no of columns matrix: ");
        int col = sc.nextInt();

        int matrix[][] = new int[row][col];
        for(int i = 0;i < row;i ++){
            for(int j = 0;j < col;j++){
                matrix[i][j] = sc.nextInt();
            }
        }

        return matrix;
    }

    static int[][] multiplication(int[][] matrix1,int[][] matrix2){
        int[][] result = new int[matrix1.length][matrix2[0].length];
        for(int i= 0;i < matrix1.length;i ++){
            int sum = 0;
            for(int j = 0;j < matrix2[0].length;j ++){
                for(int k = 0;k < matrix1[0].length;k ++){
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }

        return result;
    }

    static void display_matrix(int[][] result){
        for(int i= 0;i < result.length;i ++){
            for(int j = 0;j < result[0].length;j ++){
                System.out.print(result[i][j]+ " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        System.out.println("Enter the matrix1");
        int[][] matrix1 = getMatrix();
        System.out.println("The entered matrix1 is: ");
        display_matrix(matrix1);
        System.out.println("Enter the matrix2");
        int[][] matrix2 = getMatrix();
        System.out.println("The entered matrix2 is: ");
        display_matrix(matrix2);
        int[][] result = multiplication(matrix1,matrix2);
        System.out.println("The result is: ");
        display_matrix(result);
    }
}