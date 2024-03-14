
#include <iostream>
#include <string>
using std::string;

bool isPalindrome(string word) {
    int L = 0, R = word.size()-1;
    while (L < R) {
        if (word[L++] != word[R--])
            return false;
    }
    return true
}

int main()
{
    Str name = "Arsene";
    std::string s = "Louis";
}