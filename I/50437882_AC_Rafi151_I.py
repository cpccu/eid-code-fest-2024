# Function to find the minimum number of summands
def find_summands(n):
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
    # Read the value of n
    n = int(input())

    # Find the summands
    summands = find_summands(n)

    # Print the result
    print(len(summands))
    print(*summands)
