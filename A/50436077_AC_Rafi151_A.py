try:
    # Read the integer from input
    num = int(input())

    # Print the integer
    print(num)

except ValueError:
    # Handle the case where the input is not a valid integer
    print("Invalid input. Please enter an integer.")
