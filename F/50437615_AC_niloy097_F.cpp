#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n; cin >> n;
    map<int, int> mp;
    for(int i = 0; i < n; i++)
    {
        int x; cin >> x;
        
        mp[x]++;
    }
    int mx = 0;
    for(auto&x : mp)
    {
        mx = max(mx, x.second);
    }
    cout <<  mx << "\n";
    return 0;
}