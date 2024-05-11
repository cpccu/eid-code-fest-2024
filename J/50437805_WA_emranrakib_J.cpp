#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isValidName(const string& s) {
    int tCount = 0;
    for (char ch : s) {
        if (tolower(ch) == 't') {
            tCount++;
        } else if (!isalpha(ch)) {
            return false; // Non-alphabetic character encountered
        }
    }
    return tCount == 1; // Return true if exactly one 'T' found
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        if (isValidName(s)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
