def count_tight_words(k, n):
    if n == 1:
        return k
    
    # Initialize counts for tight and total words
    tight_count = k
    total_count = k
    
    # Calculate counts for tight and total words for each position in the word
    for i in range(1, n):
        tight_count, total_count = total_count, (tight_count + total_count) * 2 - tight_count
    
    return tight_count / total_count * 100


# Read input and process each line
while True:
    try:
        k, n = map(int, input().split())
        percentage = count_tight_words(k, n)
        print("{:.5f}".format(percentage))

    except EOFError:
        break
