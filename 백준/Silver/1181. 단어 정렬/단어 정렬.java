import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<>();
        int cnt = sc.nextInt();

        for (int i = 0; i < cnt; i++) {
            String word = sc.next();


            boolean alreadyExists = false;
            for (String existingWord : list) {
                if (existingWord.equalsIgnoreCase(word)) {
                    alreadyExists = true;
                    break;
                }
            }


            if (!alreadyExists) {
                list.add(word);
            }
        }


        list.sort(Comparator
                .comparingInt(String::length)
                .thenComparing(Comparator.naturalOrder()));


        for (String word : list) {
            System.out.println(word);
        }

        sc.close();
    }
}
