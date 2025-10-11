#include <math.h>

double magnitude(int x, int y, int z) {
    return sqrt(x*x + y*y + z*z);
}

void unitVector(int x, int y, int z, double *ux, double *uy, double *uz) {
    double mag = magnitude(x, y, z);
    *ux = x / mag;
    *uy = y / mag;
    *uz = z / mag;
}

