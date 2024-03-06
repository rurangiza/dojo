#include <iostream>

typedef int (*SumFunc)();

SumFunc add() {
    int a = 10;
    int more() {
        std::cout << a << std::endl;
    }
    return more;
}

int main() {

    

    return 0;
}