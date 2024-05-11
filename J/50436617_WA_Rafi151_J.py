# Function to check if the string is a valid spelling of Timur
def is_valid_spelling(s):
    # Check if the string length is not equal to 5
    if len(s) != 5:
        return False
    
    # Check if the first character is 'T' or 't'
    if s[0] != 'T' and s[0] != 't':
        return False
    
    # Check if the remaining characters are the permutation of 'imur'
    return sorted(s[1:].lower()) == sorted('imur')

# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Length of string s
    s = input()  # The string s

    # Check if the string is a valid spelling of Timur
    if is_valid_spelling(s):
        print("YES")
    else:
        print("NO")
