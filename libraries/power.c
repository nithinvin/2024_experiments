#include <power.h>

int power(int b, int exp) {
    int i = 0, output = 1;
    for (i = 0; i < exp; i++) {
        output = output * b;
    }
    return output;
}
