# Function to calculate the score Chef will get
def calculate_score(X, N):
    return (N * X) // 10


# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the total points for the problem and the number of test cases which pass
    X, N = map(int, input().split())
    
    # Calculate the score Chef will get
    score = calculate_score(X, N)
    
    # Print the score
    print(score)
