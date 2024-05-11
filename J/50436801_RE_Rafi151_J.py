def kadane_algorithm(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def maximal_sub_rectangle_sum(matrix):
    max_sum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        temp = [0] * cols
        for j in range(i, rows):
            for k in range(cols):
                temp[k] += matrix[j][k]
            max_sum = max(max_sum, kadane_algorithm(temp))
    
    return max_sum

# Read the size of the square two-dimensional array
N = int(input())

# Read the array elements
array = []
for _ in range(N):
    row = list(map(int, input().split()))
    array.append(row)

# Calculate and print the sum of the maximal sub-rectangle
print(maximal_sub_rectangle_sum(array))
