
#include <stdio.h>

int main() {
    
    int X,Y;
    scanf("%d",&X);
    scanf("%d",&Y);
    
    int xy = X+Y;
    
    int clearDays = 7-xy;
    
    printf("%d",clearDays);
    

    return 0;
}