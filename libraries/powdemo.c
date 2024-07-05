#include <stdio.h>
#include <power.h>

int main() {
    int base = 2, exp = 5;
    printf("%d power %d = %d\n", base, exp, power(base, exp));
}
