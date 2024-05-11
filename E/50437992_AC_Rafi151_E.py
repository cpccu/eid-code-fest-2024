# Read the input
x, y = map(int, input().split())

# Calculate the number of clear days
clear_days = 7 - x - y

# Output the result
print(clear_days)
