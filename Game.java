import java.lang.reflect.Array;
import java.util.*;

public class Game {

    public ArrayList<Integer> matrix = new ArrayList<>();
    Stack<String> matrix_stack = new Stack<>();

    //init matrix
    public Game() {
        for (int i = 0; i < 16; i++) {
            matrix.add(i, 0);
        }
        Random rand = new Random();
        int i, j;
        do {
             i = rand.nextInt(16);
             j = rand.nextInt(16);
        } while (i == j);
        matrix.set(i, 2);
        matrix.set(j, 2);
    }

    public boolean isOver() {
        if (matrix.contains(0) == true) {
            return false;
        }
        else {
            for (int i = 4; i < 16; i++) {
                if (matrix.get(i) == matrix.get(i - 4))
                    return false;
            }
            for (int i = 0; i < 16; i++) {
                if (i % 4 != 0) {
                    if (matrix.get(i) == matrix.get(i - 1))
                        return false;
                }
            }
        }
        return true;
    }

    public boolean isWin() {
        if (Collections.max(matrix) >= 2048) {
            return true;
        }
        return false;
    }

    public boolean isSame() {
        if (matrix_stack.peek().equals(matrix.toString())) {
            System.out.println();
            return true;
        }
        return false;
    }


    public void printMatrix() {
        System.out.println("+-----+-----+-----+-----+");
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j<4; j++) {
                if (matrix.get(4 * i + j) != 0) {
                    System.out.print("|");
                    for (int h = 0; h < (4 - (matrix.get(4 * i + j).toString().length())); h++) {
                        System.out.print(" ");
                    }
                    System.out.print(matrix.get(4 * i + j) + " ");
                }
                else {
                    System.out.print("|     ");
                }
            }
            System.out.println("|");
            System.out.println("+-----+-----+-----+-----+");
        }
    }

    public void move(String direction) {
        ArrayList<Integer> mergedList = new ArrayList<>();
        if (direction.equals("w")) {
            for (int n = 0;n < 16; n++) {
                int i = n;
                while (i > 3) {
                    if (matrix.get(i) != 0) {
                        if ((matrix.get(i - 4) == matrix.get(i)) && (!mergedList.contains(i))) {
                            matrix.set(i - 4, matrix.get(i)*2);
                            matrix.set(i, 0);
                            mergedList.add(i);
                            mergedList.add(i - 4);
                        }
                        else if (matrix.get(i - 4) == 0) {
                            matrix.set(i - 4, matrix.get(i));
                            matrix.set(i, 0);
                        }
                    }
                    i -= 4;
                }
            }
        }

        if (direction.equals("a")) {
            for (int n = 0;n < 16; n++) {
                int i = n;
                while (i % 4 != 0) {
                    if (matrix.get(i) != 0) {
                        if ((matrix.get(i - 1) == matrix.get(i)) && (!mergedList.contains(i))) {
                            matrix.set(i - 1, matrix.get(i)*2);
                            matrix.set(i, 0);
                            mergedList.add(i);
                            mergedList.add(i - 1);
                        }
                        else if (matrix.get(i - 1) == 0) {
                            matrix.set(i - 1, matrix.get(i));
                            matrix.set(i, 0);
                        }
                    }
                    i -= 1;
                }
            }
        }

        if (direction.equals("s")) {
            for (int n = 15;n >= 0; n--) {
                int i = n;
                while (i < 12) {
                    if (matrix.get(i) != 0) {
                        if ((matrix.get(i + 4) == matrix.get(i)) && (!mergedList.contains(i))) {
                            matrix.set(i + 4, matrix.get(i)*2);
                            matrix.set(i, 0);
                            mergedList.add(i);
                            mergedList.add(i + 4);
                        }
                        else if (matrix.get(i + 4) == 0) {
                            matrix.set(i + 4, matrix.get(i));
                            matrix.set(i, 0);
                        }
                    }
                    i += 4;
                }
            }
        }

        if (direction.equals("d")) {
            for (int n = 0;n < 16; n++) {
                int i = n;
                while (i % 4 != 3) {
                    if (matrix.get(i) != 0) {
                        if ((matrix.get(i + 1) == matrix.get(i)) && (!mergedList.contains(i))) {
                            matrix.set(i + 1, matrix.get(i)*2);
                            matrix.set(i, 0);
                            mergedList.add(i);
                            mergedList.add(i + 1);
                        }
                        else if (matrix.get(i + 1) == 0) {
                            matrix.set(i + 1, matrix.get(i));
                            matrix.set(i, 0);
                        }
                    }
                    i += 1;
                }
            }
        }
    }

    public void add() {
        ArrayList<Integer> getZeroIndex = new ArrayList<>();
        for (int i = 0; i < 16; i++) {
            if (matrix.get(i) == 0) {
                getZeroIndex.add(i);
            }
        }
        Random rand = new Random();
        matrix.set(getZeroIndex.get(rand.nextInt(getZeroIndex.size())), 2);
    }

    public void play() {
        matrix_stack.push(matrix.toString());
        while (!isOver()) {
            printMatrix();
            if (isWin()) {
                System.out.println("You win");
            }
            Scanner in = new Scanner(System.in);
            String input = in.nextLine();
            if (input.equals("w") || input.equals("a") || input.equals("s") || input.equals("d")) {
                move(input);
                if (isSame()) {
                    System.out.println("matrix is same , choose another direction!");
                    continue;
                }
                add();
                matrix_stack.push(matrix.toString());
            }
            else if (input.equals("q")) {
                System.out.println("Bye Bye!");
                return;
            }
        }
        System.out.println("Game Over! You lose!");
    }

    public static void main(String[] args) {
        Game game = new Game();
        game.play();
    }
}
