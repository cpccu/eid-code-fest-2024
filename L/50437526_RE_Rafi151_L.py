def max_subrectangle_sum(arr, n):
    max_sum = float('-inf')

    # Iterate through each row
    for i in range(n):
        # Calculate cumulative sum for current row
        for j in range(1, n):
            arr[i][j] += arr[i][j - 1]

        # Iterate through each pair of columns
        for j in range(n):
            for k in range(j, n):
                current_sum = 0
                # Calculate sum of elements in rectangle formed by rows from 0 to i and columns from j to k
                for l in range(i + 1):
                    current_sum += arr[l][k] - (arr[l][j - 1] if j > 0 else 0)
                    max_sum = max(max_sum, current_sum)

    return max_sum

# Read input
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Calculate and print the sum of maximal sub-rectangle
print(max_subrectangle_sum(arr, n))
