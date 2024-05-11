def kadane(arr):
    max_sum = current_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
    return max_sum

def maximal_subrectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    # Iterate over each column as the left boundary
    for left in range(cols):
        # Initialize an array to store the cumulative sums of each row
        cum_row_sum = [0] * rows

        # Iterate over each column as the right boundary
        for right in range(left, cols):
            # Update the cumulative sums of each row
            for i in range(rows):
                cum_row_sum[i] += matrix[i][right]

            # Apply Kadane's algorithm to find the maximum sum subarray for this subrectangle
            max_subarray_sum = kadane(cum_row_sum)

            # Update the maximum sum if a larger sum is found
            max_sum = max(max_sum, max_subarray_sum)

    return max_sum

# Read input
N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the maximal subrectangle sum
result = maximal_subrectangle(matrix)

# Output the result
print(result)
