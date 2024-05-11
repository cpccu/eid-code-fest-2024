#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int MAX_SIZE = 100;

int kadane(const vector<int>& arr, int n) {
    int max_sum = arr[0], current_max = arr[0];
    
    for (int i = 1; i < n; ++i) {
        current_max = max(arr[i], current_max + arr[i]);
        max_sum = max(max_sum, current_max);
    }
    
    return max_sum;
}

int maxSubRectangleSum(vector<vector<int>>& matrix, int N) {
    int max_sum = numeric_limits<int>::min();
    
    for (int left = 0; left < N; ++left) {
        vector<int> temp(N, 0);
        
        for (int right = left; right < N; ++right) {
            for (int i = 0; i < N; ++i) {
                temp[i] += matrix[i][right];
            }
            
            int current_max = kadane(temp, N);
            max_sum = max(max_sum, current_max);
        }
    }
    
    return max_sum;
}

int main() {
    int N;
    cin >> N; // Input the size of the square 2D array
    
    vector<vector<int>> matrix(N, vector<int>(N));
    
    // Input the array elements
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> matrix[i][j];
        }
    }
    
    // Calculate and output the sum of maximal sub-rectangle
    cout << maxSubRectangleSum(matrix, N) << endl;
    
    return 0;
}
