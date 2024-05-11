#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> roundNumbers;
        int position = 1;
        
        while (n > 0) {
            int digit = n % 10;
            if (digit != 0) {
                roundNumbers.push_back(digit * position);
            }
            n /= 10;
            position *= 10;
        }

        // Output the minimum number of summands
        cout << roundNumbers.size() << endl;

        // Output the round numbers
        for (int num : roundNumbers) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
