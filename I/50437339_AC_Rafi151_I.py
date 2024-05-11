# Function to represent the number n as a sum of round numbers
def represent_as_sum_of_round_numbers(n):
    summands = []
    multiplier = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            summands.append(digit * multiplier)
        n //= 10
        multiplier *= 10
    return summands

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Read the number
    summands = represent_as_sum_of_round_numbers(n)  # Represent the number as a sum of round numbers
    print(len(summands))  # Print the number of summands
    print(*summands)  # Print the round numbers
