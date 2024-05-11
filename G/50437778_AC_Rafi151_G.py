# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the distance to the office
    x = int(input())
    
    # Calculate the total distance traveled in a week
    total_distance = 2 * x * 5
    
    # Print the result
    print(total_distance)
