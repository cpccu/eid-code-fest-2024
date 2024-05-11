try:
    # Read the two integers from input
    a, b = map(int, input().split())

    # Calculate their sum
    total = a + b

    # Print the sum
    print(total)

except ValueError:
    # Handle the case where the input is not valid integers
    print("Invalid input. Please enter integers.")
