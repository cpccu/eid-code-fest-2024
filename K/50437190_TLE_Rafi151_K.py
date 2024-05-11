def count_tight_words(k, n):
    if n == 1:
        return k  # Each digit is tight by itself
    tight_count = 0
    for i in range(10):
        if i - 1 >= 0:
            tight_count += count_tight_words(k, n - 1)
        if i + 1 < 10:
            tight_count += count_tight_words(k, n - 1)
    return tight_count

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
    total_words = k ** n
    tight_words = count_tight_words(k, n)
    percentage = (tight_words / total_words) * 100
    print("{:.5f}".format(percentage))
