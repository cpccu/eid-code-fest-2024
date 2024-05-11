
n = int(input())
coins = list(map(int, input().split()))


coin_counts = {}
for coin in coins:
    if coin in coin_counts:
        coin_counts[coin] += 1
    else:
        coin_counts[coin] = 1


max_frequency = max(coin_counts.values())


print(max_frequency)
