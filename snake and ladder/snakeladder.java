import java.util.*;
import java.time.LocalTime;

public class snakeladder {
    public static void main(String[] args) {
        Random rand = new Random();
        int randomNumber = rand.nextInt(1,6);

        Map<Integer,Integer> snake = new HashMap<>();
        snake.put(17,7);
        snake.put(54,34);
        snake.put(17,7);
        snake.put(17,7);
        snake.put(17,7);
        snake.put(17,7);
        snake.put(17,7);
        snake.put(17,7);

        Map<Integer,Integer> ladder = new HashMap<>();
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);
        ladder.put(21,34);


        
    }
}
