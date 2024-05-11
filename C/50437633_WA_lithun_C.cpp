#include <stdio.h>

int main() {
    int alice_card, bob_card;

    scanf("%d", &alice_card);

    scanf("%d", &bob_card);

    if (alice_card == bob_card) {
        printf("It's a draw!\n");
    } else if ((alice_card == 1 && bob_card != 1) || (alice_card > bob_card && bob_card != 1)) {
        printf("Alice wins!\n");
    } else {
        printf("Bob wins!\n");
    }

    return 0;
}
