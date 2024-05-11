#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a, b; cin >> a >> b;
    if(a != 1 and b != 1 and a > b) cout << "Alice" << endl;
    else if(a != 1 and b != 1 and a < b) cout << "Bob" << endl;
    else if(a != 1 and b != 1 and a == b) cout << "Draw" << endl;
    else if(a == 1 and b == 1) cout << "Draw" << endl;
    else if(a == 1) cout << "Alice" << endl;
    else if(b == 1) cout << "Bob" << endl;
    return 0;
}