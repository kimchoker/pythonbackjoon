import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt(); int B = sc.nextInt();
        int B1 = (B / 100) * 100;
        int B2 = ((B % 100) / 10) * 10;
        int B3 = ((B % 100) % 10);
        System.out.println(A * B3);
        System.out.println((A * B2)/10);
        System.out.println((A * B1)/100);
        System.out.println(A * B);
    }
}
