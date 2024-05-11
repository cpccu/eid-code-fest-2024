# Function to count the number of tight words of length n
def count_tight_words(k, n):
    # If n is 1, all words are tight
    if n == 1:
        return k

    # Initialize count of tight words with the number of possible starting digits
    count = k

    # Calculate the number of tight words recursively
    for _ in range(n - 1):
        count *= min(2, k)

    return count

# Function to calculate the percentage of tight words
def calculate_percentage(k, n):
    # Calculate the total number of possible words
    total_words = k ** n

    # Calculate the number of tight words
    tight_words = count_tight_words(k, n)

    # Calculate the percentage
    percentage = (tight_words / total_words) * 100

    return percentage

# Read the input
inputs = []
while True:
    try:
        k, n = map(int, input().split())
        inputs.append((k, n))
    except EOFError:
        break

# Process each input and output the result
for k, n in inputs:
    percentage = calculate_percentage(k, n)
    print("{:.5f}".format(percentage))
