# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the distance between home and office for the current test case
    X = int(input())
    
    # Calculate the total distance traveled in a week (assuming office is open 5 days a week)
    total_distance = 2 * X * 5
    
    # Output the total distance traveled in a week
    print(total_distance)
