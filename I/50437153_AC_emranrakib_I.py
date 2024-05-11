# Function to represent the number as a sum of round numbers
def sum_of_round_numbers(n):
    # Convert the number to a string for easier manipulation of digits
    n_str = str(n)
    
    # Initialize a list to store the round numbers
    round_numbers = []
    
    # Iterate through each digit of the number from right to left
    for i in range(len(n_str) - 1, -1, -1):
        digit = int(n_str[i])
        # If the digit is not zero, append it multiplied by the appropriate power of 10
        if digit != 0:
            round_numbers.append(str(digit * 10**(len(n_str) - i - 1)))
    
    
    print(len(round_numbers))
    print(" ".join(round_numbers))


t = int(input())


for _ in range(t):
  
    n = int(input())
    
   
    sum_of_round_numbers(n)
