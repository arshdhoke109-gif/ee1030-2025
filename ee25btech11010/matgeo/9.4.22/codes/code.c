#include <math.h>

double find_k() {
    double k1, k2;     
    double a, b, c;    
    double D;          

    // Equation: 4k^2 - 24k = 0
    a = 4;
    b = -24;
    c = 0;

 
    D = b * b - 4 * a * c;

    k1 = (-b + sqrt(D)) / (2 * a);
    k2 = (-b - sqrt(D)) / (2 * a);

    // k = 0 or 6, but k = 0 makes equation invalid
    if (k1 != 0)
        return k1;
    else
        return k2;
}
