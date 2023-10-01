#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f;
double x;


int main()
{

    double x = 0.0;
    double y;

    double s;
    printf("Enter s -> ");
    scanf("%lf", &s);

    while (0<=x && x<=1){
        y = cos(x+ pow(x, 3));
        printf("%f %f\n", x, y);
    }
    while(1 < x && x <= 2){
        y = exp(pow(-x,2))-pow(x,2)+2*x;
        printf("%f %f\n", x, y);
    }
    return 0;
}