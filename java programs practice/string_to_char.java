import java.util.*;
public class string_to_char {
    public static void main(String[] args) {
        String str = "Hello Prasanth";
        char[] ch = new char[str.length()];

        for(int i = 0;i < str.length();i++){
            ch[i] = str.charAt(i);
        }

        for (char x:ch){
            System.out.println(x);
        }
    }
}
