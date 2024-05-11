# Function to represent the number n as a sum of round numbers
def represent_as_sum_of_round_numbers(n):
    digits = []  # List to store the round numbers
    
    # Convert the number to a string and iterate through its digits
    for i, digit in enumerate(str(n)[::-1]):
        # If the digit is not '0', add the round number to the list
        if digit != '0':
            digits.append(int(digit) * 10**i)
    
    return digits


# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Number n
    
    # Represent the number n as a sum of round numbers
    round_numbers = represent_as_sum_of_round_numbers(n)
    
    # Print the minimum number of summands followed by the round numbers
    print(len(round_numbers))
    print(*round_numbers)
