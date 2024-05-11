# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the total points for the problem and the number of test cases passed by Chef
    X, N = map(int, input().split())
    
    # Calculate the score for Chef
    score = (X // N) * N
    
    # Output the score
    print(score)
