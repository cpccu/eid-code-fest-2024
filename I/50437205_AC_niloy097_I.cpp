#include<bits/stdc++.h>
#define ROCKET ios :: sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
#define ll long long int
#define fr(x, s, e, b) for(ll x = s; x < e; x = x + b)
#define rfr(x, s, e, b) for(ll x = s; x >= e; x = x - b)
#define efr(val, where) for(auto& val : where)
#define all(x) x.begin(), x.end()
#define el '\n'
#define vtr vector
#define vl vector<int>
#define vll vector<long long int>
#define str string
#define pb push_back
#define MOD (int)1e9 + 7
#define N (int)1e5 + 7
#define imax INT_MAX
#define imin INT_MIN
#define pr pair<int, int>
#define hash map<int, int>
#define dnin ll n; cin >> n
using namespace std;
bool isPalindrom(string x)
{
    int i = 0;
    int j = x.size() -1;
    while(i < j)
    {
        if(x[i] != x[j]) return false;
        i++;
        j--;
    }
    return true;
}
bool isEven(ll n)
{
    return n % 2 == 0;
}
bool isOdd(ll n)
{
    return n % 2 != 0;
}
int findXorOfN(int n)
{
   if(n % 4 == 0) return n;
   else if(n % 4 == 1) return 1;
   else if(n % 4 == 2) return n + 1;
   else if(n % 4 == 3) return 0;
}
bool isPrime(int n)
{
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    for(int i = 3; i * i <= n; i += 2)
    {
        if(n % i == 0) return false;
    }
    return true;
}
ll gcd(ll a, ll b)
{
    if(b == 0) return a;
    return gcd(b, a % b);
}
vll getBin(ll n)
{
    vll v;
    while(n)
    {
        int bin = n & 1;
        v.pb(bin);
        n = n >> 1;
    }
    reverse(all(v));
    return v;
}
vector<ll> primeFactorization(ll n)
{
    vector<ll> factors;
    for(ll i = 2; i * i <= n; i++)
    {
        ll cnt = 0;
        while(n % i == 0)
        {
            cnt++;
            n /= i;
            factors.push_back(i);
        }
    }
    if(n > 1) factors.push_back(n);
    return factors;
}
ll digitSum(ll n)
{
    ll sum = 0;
       string num = to_string(n);
       for(int i = 0; i < num.size(); i++)
       {
           sum += (num[i] - '0');
    }
    return sum;
}
void solve()
{
    int n; cin >> n;
    vl v;
    str x = to_string(n);
    int base = (int)pow(10, x.size()-1);
    fr(i, 0, x.size(), 1)
    {
        int numb = (x[i] - '0') * base;
        if(numb != 0) v.pb(numb);
        base /= 10;
    }
    cout << v.size() << el;
    efr(x, v) cout << x << " ";
    cout << el;
}
signed main()
{
    ROCKET

    int t = 1;
    cin >> t;
    while(t--) solve();
    
    return 0;
}