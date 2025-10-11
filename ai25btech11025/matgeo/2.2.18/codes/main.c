#include <stdio.h>
#include <math.h>

double magnitude(int x, int y, int z) {
    return sqrt(x*x + y*y + z*z);
}

void unitVector(int x, int y, int z) {
    double mag = magnitude(x, y, z);
    printf("Unit normal vector = (%.3f)i + (%.3f)j + (%.3f)k\n", 
           x/mag, y/mag, z/mag);
}

int main() {
    int a = 1, b = 2, c = 3;  // coefficients of x, y, z
    unitVector(a, b, c);
    return 0;
}

