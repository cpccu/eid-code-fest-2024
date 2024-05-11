# Function to find the maximum sum subarray in a 1-dimensional array using Kadane's algorithm
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Function to find the maximal sub-rectangle sum
def maximal_subrectangle(matrix):
    max_sum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Iterate through each row
    for i in range(rows):
        # Initialize an array to store the cumulative sums of each column
        cum_col_sum = [0] * cols
        
        # Iterate through each row starting from the current row
        for j in range(i, rows):
            # Update the cumulative sums of each column
            for k in range(cols):
                cum_col_sum[k] += matrix[j][k]
            
            # Apply Kadane's algorithm to find the maximum sum subarray for this subrectangle
            max_subarray_sum_in_row = max_subarray_sum(cum_col_sum)
            
            # Update the max_sum if the maximum sum subarray in this row is greater than max_sum
            max_sum = max(max_sum, max_subarray_sum_in_row)
    
    return max_sum

# Read input
N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the maximal sub-rectangle sum
result = maximal_subrectangle(matrix)

# Output the result
print(result)
