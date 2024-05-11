# Function to check if the string is a valid spelling of Timur's name
def is_valid_spelling(s):
    # Check if the length of the string is exactly 5
    if len(s) != 5:
        return False
    
    # Check if the first letter is uppercase 'T'
    if s[0] != 'T':
        return False
    
    # Check if all other letters are lowercase
    if not s[1:].islower():
        return False
    
    return True

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the string
    n = int(input())
    # Read the string
    s = input()
    
    # Check if the string is a valid spelling of Timur's name
    if is_valid_spelling(s):
        print("YES")
    else:
        print("NO")
