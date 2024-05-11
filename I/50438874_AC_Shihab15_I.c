#include <stdio.h>

int main() {
    int test;
    scanf("%d", &test); 

    while (test--) {
        int n;
        scanf("%d", &n); 
        int count = 0; 
        int multiplier = 1; 
        
      
        int roundNumbers[4] = {0};
        
        while (n > 0) {
            int digit = n % 10; 
            
            if (digit != 0) {
                roundNumbers[count++] = digit * multiplier; 
            }
            
            n /= 10; 
            multiplier *= 10; 
        }

        printf("%d\n", count);
        
        
        for (int i = 0; i < count; i++) {
            printf("%d ", roundNumbers[i]);
        }
        
        printf("\n");
    }

    return 0;
}
