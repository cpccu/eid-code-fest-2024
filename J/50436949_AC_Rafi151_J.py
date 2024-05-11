def is_valid_spelling(s):
    # Correct spelling of the name 'Timur'
    correct_spelling = 'Timur'
    
    # Check if the string is a permutation of 'Timur' and has an uppercase 'T'
    return sorted(s) == sorted(correct_spelling) and s.count('T') == 1 and s.count('t') == 0

# Read the number of test cases
t = int(input().strip())

# Iterate over each test case
for _ in range(t):
    # Read the length of the string (not used in this solution)
    n = int(input().strip())
    
    # Read the string
    s = input().strip()
    
    # Check if the string is a valid spelling of 'Timur'
    if is_valid_spelling(s):
        print("YES")
    else:
        print("NO")
