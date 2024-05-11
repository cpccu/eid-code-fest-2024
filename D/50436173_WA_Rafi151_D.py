try:
    # Read the syllable counts of the three phrases from input
    a = int(input())
    b = int(input())
    c = int(input())

    # Check if it's possible to construct a Haiku
    if a == 5 and b == 7 and c == 5:
        print("YES")
    else:
        print("NO")

except ValueError:
    # Handle the case where the input is not valid integers
    print("Invalid input. Please enter integers.")
