#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T); 
    while (T--) {
        int X, N;
        scanf("%d %d", &X, &N); 

        
        int score = (N * X) / 10;
        printf("%d\n", score);
    }
    return 0;
}
