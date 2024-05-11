#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T); // Input the number of test cases
    while (T--) {
        int X;
        scanf("%d", &X); // Input the distance between Chef's home and office

        // Total distance traveled in a week = 2 * distance to the office * number of working days
        int total_distance = 2 * X * 5;
        printf("%d\n", total_distance);
    }
    return 0;
}
