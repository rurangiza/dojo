// #include <bits/stdc++.h>
#include "stdc++.h"
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<string> v;
    while (n-- > 0) {
        string x;
        cin >> x;
        if (x.size() > 10)
            x = x[0] + to_string(x.size()-2) + x[x.size()-1];
        v.push_back(x);
    }
    cout << endl;
    for (string s : v)
        cout << s << "\n";
    
    return 0;
}