#include <stdio.h>
int main(){

    int a = 90;
    char b = 'b';
    char* c = "ceeded";

    printf("int: %lu\nchar: %lu\nstr: %c\n",
        sizeof(a), sizeof(b), *c);

    return 0;
}