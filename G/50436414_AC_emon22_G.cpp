#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T; // Number of test cases
    
    while (T--) {
        int X;
        cin >> X;
        
        int total_distance = 2 * X; // Round trip distance
        int weekly_distance = total_distance * 5; 
        
        cout << weekly_distance << endl;
    }
    return 0;
}
