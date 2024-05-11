def kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_sub_rectangle(arr):
    max_sum = float('-inf')
    rows = len(arr)
    cols = len(arr[0])
    
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += arr[i][right]
            max_sum = max(max_sum, kadane(temp))
    
    return max_sum

# Read the size of the square two-dimensional array
N = int(input())

# Read the elements of the array
arr = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the sum of the maximal sub-rectangle
print(max_sub_rectangle(arr))
