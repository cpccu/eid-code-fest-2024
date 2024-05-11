# Read input
n = int(input())
coins = list(map(int, input().split()))

# Count the frequency of each coin value
coin_counts = {}
for coin in coins:
    if coin in coin_counts:
        coin_counts[coin] += 1
    else:
        coin_counts[coin] = 1

# Find the maximum frequency
max_frequency = max(coin_counts.values())

# Output the minimum number of pockets needed
print(max_frequency)
