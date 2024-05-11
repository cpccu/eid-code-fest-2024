
#include <stdio.h>

int main() {
    
    int X,T;
    scanf("%d",&T);
    
    
    while(T-->0){
        scanf("%d",&X);
        int updown = X+X;
        int km = updown*5;
        printf("%d",km);
    }
    

    return 0;
}