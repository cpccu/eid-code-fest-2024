#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n; cin >> n;
    vector<int> v(n);
    string x = to_string(n);
    int base = (int)pow(10, x.size()-1);
    for(int i = 0; i < x.size(); i++)
    {
        int numb = (x[i] - '0') * base;
        if(numb != 0) v.push_back(numb);
        base /= 10;
    }
    cout << v.size() << endl;
    for(auto&x : v) cout << x << " ";
    cout << endl;
    return 0;
}