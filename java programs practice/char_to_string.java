import java.io.*;
import java.util.*;
public class char_to_string{
    public static void main(String[] args) {
        char c1 = 'a';
        char c2 = 'b';
        char c3 = 'c';

        String s1 = String.valueOf(c1);
        System.out.println("Using valueOf(): " + s1 );

        String s2 = Character.toString(c2);
        System.out.println("Using toString(): " + s2);

        String s3 = "" + c3;
        System.out.println("Adding with empty string: " + s3);
    }
}