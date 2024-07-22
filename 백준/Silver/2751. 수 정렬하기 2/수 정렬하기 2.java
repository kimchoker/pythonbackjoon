import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> list = new ArrayList<>();

        int cnt = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < cnt; i++) {
            int num = Integer.parseInt(br.readLine().trim());
            list.add(num);
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for (Integer num : list) {
            sb.append(num).append("\n");
        }
        System.out.print(sb.toString());
    }
}
