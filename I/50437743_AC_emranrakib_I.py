t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Input number
    
    round_numbers = []  # List to store round numbers
    position = 1  # Position multiplier
    
    while n > 0:
        digit = n % 10  # Extract the last digit
        if digit != 0:
            round_numbers.append(digit * position)  # Construct round number
        n //= 10  # Remove the last digit
        position *= 10  # Update position multiplier
    
    # Output the minimum number of summands
    print(len(round_numbers))
    
    # Output the round numbers
    print(*round_numbers)
