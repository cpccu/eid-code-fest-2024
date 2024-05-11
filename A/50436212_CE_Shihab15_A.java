
import java.util.Scanner;

public class NewClass {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int input = sc.nextInt();
        
        if(-200000000<input && input<200000000){
            System.out.println(input);
        }
    }
    
}
