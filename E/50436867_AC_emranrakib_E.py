# Read the number of rainy and cloudy days
X, Y = map(int, input().split())

# Total number of days in the week
total_days = 7

# Calculate the number of clear days
clear_days = total_days - X - Y

# Output the number of clear days
print(clear_days)
