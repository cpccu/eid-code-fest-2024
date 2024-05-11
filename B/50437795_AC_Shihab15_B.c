
#include <stdio.h>

int main() {
    
    int A,B;
    scanf("%d",&A);
    scanf("%d",&B);
    
    if(-200000000<A && B<200000000){
        int sum = A+B;
        printf("%d",sum);
    }

    return 0;
}