import java.util.Scanner;

public class solution{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        scanner.close();
        
        int result = 0;
        
        if (A % 4 == 0 && A % 100 != 0 || A % 400 == 0) {
            result = 1;
        }
        
        System.out.println(result);
    }
}
