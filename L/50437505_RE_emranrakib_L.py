#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Function to find the maximum sum subarray in a 1-dimensional array using Kadane's algorithm
int maxSubArraySum(const vector<int>& arr) {
    int maxSum = INT_MIN;
    int currentSum = 0;
    for (int num : arr) {
        currentSum = max(num, currentSum + num);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

// Function to find the maximal sub-rectangle sum
int maximalSubrectangle(const vector<vector<int>>& matrix) {
    int maxSum = INT_MIN;
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    for (int i = 0; i < rows; ++i) {
        vector<int> cumColSum(cols, 0);
        
        for (int j = i; j < rows; ++j) {
            for (int k = 0; k < cols; ++k) {
                cumColSum[k] += matrix[j][k];
            }
            
            int maxSubarraySumInRow = maxSubArraySum(cumColSum);
            maxSum = max(maxSum, maxSubarraySumInRow);
        }
    }
    
    return maxSum;
}

int main() {
    int N;
    cin >> N;

    vector<vector<int>> matrix(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> matrix[i][j];
        }
    }

    // Find the maximal sub-rectangle sum
    int result = maximalSubrectangle(matrix);

    // Output the result
    cout << result << endl;

    return 0;
}
