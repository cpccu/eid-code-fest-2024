#include <iostream>

using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    // Check if the sum of syllables matches the Haiku pattern (5, 7, 5)
    if (A + B + C == 17) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
