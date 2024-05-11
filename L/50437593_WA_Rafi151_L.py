def max_sub_rectangle_sum(matrix):
    def max_sub_array_sum(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            max_sum = max(max_sum, max_sub_array_sum(temp))

    return max_sum

# Sample input
N = 4
matrix = [
    [0, -2, -7, 0],
    [9, 2, -6, 2],
    [-4, 1, -4, 1],
    [-1, 8, 0, -2]
]

# Output the sum of the maximal sub-rectangle
print(max_sub_rectangle_sum(matrix))
