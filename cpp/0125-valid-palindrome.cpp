
#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;

class Solution {
    public:
        static bool isPalindrome(string word) {
            int L = 0, R = word.size()-1;
            while (L < R) {
                if (word[L++] != word[R--])
                    return false;
            }
            return true;
        }
};

int main()
{
    string str = "helleh";
    bool result = Solution::isPalindrome(str);
    cout << result << endl;
}