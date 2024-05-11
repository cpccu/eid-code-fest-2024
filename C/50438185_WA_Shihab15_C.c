
#include <stdio.h>

int main() {
    
    int A,B;
    scanf("%d",&A);
    scanf("%d",&B);
    
    if(A>0 && A<=13 && B>0 && B<=13){
        if(A>B || A==1){
        printf("Alice");
    }else if(B>A || B==1){
        printf("Bob");
    }else if(A==B){
        printf("Draw");
    }
    }
    

    return 0;
}