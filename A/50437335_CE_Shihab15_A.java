package NewClass;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NewClass { // Class name matches the file name
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        // Read input as string
        String inputString = reader.readLine();
        
       
        int A = Integer.parseInt(inputString);
        
        if(A>-200000000 && A<200000000){
            System.out.println(A);
        }
    }

}
