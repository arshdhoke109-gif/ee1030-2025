#include <stdio.h>
#include <math.h>

void solve_conic() {
    double a_ellipse = 5.0, b_ellipse = 4.0;
    double e_E = sqrt(1 - (b_ellipse * b_ellipse) / (a_ellipse * a_ellipse));
    double e_H = 1.0 / e_E;
    double eH2 = e_H * e_H;

    double x = 3.0;
    double lambda1_H = 1.0 / (x * x);
    double lambda2_H = lambda1_H / (1 - eH2);

    double a_H = sqrt(1.0 / lambda1_H);
    double b_H = sqrt(-1.0 / lambda2_H);
    double c_H = sqrt(a_H * a_H + b_H * b_H);

}