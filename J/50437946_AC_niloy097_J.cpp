#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string x, idol = "Timur";
        cin >> x;
        vector<int> iHash(52, 0);
        vector<int> xHash(52, 0);
        for (int i = 0; i < idol.size(); i++)
        {
            if (idol[i] >= 'A' && idol[i] <= 'Z')
                iHash[idol[i] - 'A']++;
            else
                iHash[idol[i] - 'a' + 26]++;
        }
        for (int i = 0; i < x.size(); i++)
        {
            if (x[i] >= 'A' && x[i] <= 'Z')
                xHash[x[i] - 'A']++;
            else
                xHash[x[i] - 'a' + 26]++;
        }
        if (iHash == xHash)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}