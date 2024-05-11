# Function to count the number of tight words of length n over the alphabet {0, 1, ..., k}
def count_tight_words(k, n):
    # Initialize a dynamic programming table to store the count of tight words
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the base cases for n = 1
    for digit in range(k + 1):
        dp[0][digit] = 1

    # Iterate through the length of the word
    for i in range(1, n):
        # Iterate through each digit of the alphabet
        for digit in range(k + 1):
            # Count the number of tight words ending with the current digit
            for diff in [-1, 0, 1]:
                if 0 <= digit + diff <= k:
                    dp[i][digit] += dp[i - 1][digit + diff]

    # Sum up the counts for all digits for length n
    total_tight_words = sum(dp[n - 1])

    return total_tight_words

# Read input
while True:
    try:
        k, n = map(int, input().split())

        # Count the total number of words of length n over the alphabet {0, 1, ..., k}
        total_words = (k + 1) ** n

        # Count the number of tight words of length n over the alphabet {0, 1, ..., k}
        tight_words = count_tight_words(k, n)

        # Calculate the percentage of tight words with 5 fractional digits
        percentage = (tight_words / total_words) * 100

        # Output the percentage with 5 fractional digits
        print("{:.5f}".format(percentage))

    except EOFError:
        break
