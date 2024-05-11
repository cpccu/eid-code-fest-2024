#include <stdio.h>

int main() {
    int A, B, C;
    
    // Read the number of syllables in each phrase
    scanf("%d %d %d", &A, &B, &C);

    // Check if the total number of syllables matches the Haiku pattern
    if (A + B + C == 17 && A <= 5 && B <= 7 && C <= 5) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
