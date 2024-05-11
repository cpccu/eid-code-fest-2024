def kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_subrectangle_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    for i in range(rows):
        temp = [0] * cols
        for j in range(i, rows):
            for k in range(cols):
                temp[k] += matrix[j][k]
            max_sum = max(max_sum, kadane(temp))
    return max_sum

# Read input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the maximum sum subrectangle
print(max_subrectangle_sum(matrix))
