from collections import Counter

# Read input
n = int(input())
coins = list(map(int, input().split()))

# Count the frequency of each coin value
coin_frequency = Counter(coins)

# Find the maximum frequency
max_frequency = max(coin_frequency.values())

# Print the maximum frequency, which represents the minimum number of pockets needed
print(max_frequency)
