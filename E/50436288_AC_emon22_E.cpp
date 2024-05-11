#include <iostream>
using namespace std;

int main() {
    int X, Y;
    cin >> X >> Y;
    int clear_days = 7 - X - Y;
    cout << clear_days << endl;
    return 0;
}
