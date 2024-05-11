try:
    # Read Alice's and Bob's cards from input
    alice_card, bob_card = map(int, input().split())

    # Define the strength of cards
    card_strength = {
        1: 14,  # Ace
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,  # Jack
        12: 12,  # Queen
        13: 13   # King
    }

    # Compare the strength of Alice's and Bob's cards
    if card_strength[alice_card] > card_strength[bob_card]:
        print("Alice")
    elif card_strength[alice_card] < card_strength[bob_card]:
        print("Bob")
    else:
        print("Draw")

except ValueError:
    # Handle the case where the input is not valid integers
    print("Invalid input. Please enter integers.")
