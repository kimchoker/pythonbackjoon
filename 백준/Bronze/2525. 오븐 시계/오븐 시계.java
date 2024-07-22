import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nowH = sc.nextInt(); int nowM = sc.nextInt(); int time = sc.nextInt();
        int timeH = 0;
        int timeM = 0;

        if(time > 60) {
            timeH = time / 60;
            timeM = time % 60;
        } else {
            timeM = time;
        }

        if(nowM + timeM >  59) {
            nowM = nowM + timeM - 60;
            nowH++;
        } else {
            nowM = nowM + timeM;
        }

        if(nowH + timeH > 23) {
            nowH = nowH + timeH - 24;
        } else {
            nowH = nowH + timeH;
        }

        System.out.print(nowH + " ");
        System.out.print(nowM);

    }
}