#include <iostream>
#include <iomanip>

using namespace std;

// Function to count the number of tight words of length n over the alphabet {0, 1, ..., k}
int countTightWords(int k, int n) {
    // Base case: for n = 1, there are k + 1 tight words
    if (n == 1) return k + 1;
    
    // Initialize a 2D array to store the count of tight words ending with each digit
    int tightCount[10][101] = {0};
    
    // For length 1, all single-digit numbers are tight words
    for (int i = 0; i <= k; ++i) {
        tightCount[i][1] = 1;
    }
    
    // Fill the tightCount array iteratively using dynamic programming
    for (int len = 2; len <= n; ++len) {
        for (int digit = 0; digit <= k; ++digit) {
            for (int diff = -1; diff <= 1; ++diff) {
                int prevDigit = digit + diff;
                if (prevDigit >= 0 && prevDigit <= k) {
                    tightCount[digit][len] += tightCount[prevDigit][len - 1];
                }
            }
        }
    }
    
    // Sum up the counts for all digits for length n
    int totalCount = 0;
    for (int digit = 0; digit <= k; ++digit) {
        totalCount += tightCount[digit][n];
    }
    
    return totalCount;
}

int main() {
    int k, n;
    while (cin >> k >> n) {
        // Calculate the total number of words of length n over the alphabet {0, 1, ..., k}
        int totalWords = k + 1;
        for (int i = 1; i < n; ++i) {
            totalWords *= (k + 1);
        }
        
        // Calculate the number of tight words of length n
        int tightWords = countTightWords(k, n);
        
        // Calculate the percentage of tight words
        double percentage = (double) tightWords / totalWords * 100;
        
        // Output the percentage with 5 fractional digits
        cout << fixed << setprecision(5) << percentage << endl;
    }
    return 0;
}
