#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

// Function to check if s is a valid spelling of Timur's name
bool isValidName(char *s, int n) {
    int tCount = 0;
    for (int i = 0; i < n; i++) {
        if (tolower(s[i]) == 't') {
            tCount++;
        } else if (!isalpha(s[i])) {
            return false; // Non-alphabetic character encountered
        }
    }
    return tCount == 1; // Return true if exactly one 'T' found
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);
        char s[11];
        scanf("%s", s);

        if (isValidName(s, n)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}
