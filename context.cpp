#include <bits/stdc++.h>
using namespace std;

int f(int x, int y) {
    return (x + y) % pow(10, 8);
}

int main() {
    int N; cin >> N;
    int nums[k];
    for (for int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int total;
    for (int i = 0; i < N-1; i++) {
        for (int j = i+1; j < N; j++) {
            total += f(nums[i], nums[j]);
        }
    }
    cout << total;
    return 0;
}