#include <stdio.h>

int main() {
    int alice_card, bob_card;

    // Input Alice's card
    printf("Enter Alice's card number (1-13): ");
    scanf("%d", &alice_card);

    // Input Bob's card
    printf("Enter Bob's card number (1-13): ");
    scanf("%d", &bob_card);

    // Determine the outcome
    if (alice_card == bob_card) {
        printf("It's a draw!\n");
    } else if ((alice_card == 1 && bob_card != 1) || (alice_card > bob_card && bob_card != 1)) {
        printf("Alice wins!\n");
    } else {
        printf("Bob wins!\n");
    }

    return 0;
}
