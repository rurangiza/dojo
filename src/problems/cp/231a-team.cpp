// #include <bits/stdc++.h>
#include "stdc++.h"
using namespace std;

int main() {
    int n, a, b , c, res = 0;
    
    cin >> n;
    while (n-- > 0) {
        cin >> a >> b >> c;
        if ((a + b + c) > 1) {
            res++;
        }
    }
    cout << res;
    return 0;
}