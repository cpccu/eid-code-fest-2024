def count_tight_words(k, n):
    # Initialize dp array
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: initialize first row of dp array
    for j in range(1, k + 1):
        dp[0][j] = 1
    
    # Compute dp array
    for i in range(1, n):
        for j in range(1, k + 1):
            for x in range(max(1, j - 1), min(k, j + 2) + 1):
                dp[i][j] += dp[i - 1][x]
    
    # Compute total count of tight words
    total_count = sum(dp[-1][1:])
    
    # Compute percentage
    percentage = (total_count / (k ** n)) * 100
    
    return percentage

# Read input
inputs = []
while True:
    try:
        k, n = map(int, input().split())
        inputs.append((k, n))
    except EOFError:
        break

# Process each input and calculate the percentage of tight words
for k, n in inputs:
    percentage = count_tight_words(k, n)
    print("{:.5f}".format(percentage))
