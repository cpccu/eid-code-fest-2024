#include<bits/stdc++.h>
using namespace std;
int main()
{

    vector<int> v(3);
    for (int i = 0; i < 3; i++) cin >> v[i];      
    int cnt1 = 0;
    int cnt2 = 0;
    for(int i = 0; i < 3; i++)
    {
        if (v[i] == 5)
            cnt1++;
        if (v[i] == 7)
            cnt2++;
    }
    if (cnt1 == 2 and cnt2 == 1)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}