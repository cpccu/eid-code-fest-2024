# Function to find the maximum sum subarray in a 1-dimensional array
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
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
        # Initialize a temporary array to store the maximum sum sub-array ending at each position
        temp = [0] * cols
        
        # Iterate through each column
        for j in range(cols):
            # Update the value of the current element to include the maximum sum sub-array ending at the previous element
            if j == 0:
                temp[j] = matrix[i][j]
            else:
                temp[j] = max(matrix[i][j], matrix[i][j] + temp[j - 1])
            
            # Update max_sum if the current element's value is greater than max_sum
            max_sum = max(max_sum, temp[j])
    
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
