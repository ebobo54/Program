#include <stdio.h>
#include <math.h>

int main()
{
    double n,y,s,x = 0.0;
    printf("Enter number-> ");
    scanf("%lf", &s);
    n = s / 2.0;
    
    for(x = 0.0; x <= 2.0 + n; x = x + s)
    {
        if(x >= 0 && x <= 1)
            y = cos(x + x*x*x);
        else
            y = exp(-x*x) - (x*x) + 2.0 * x;
        printf("%f\t%f\n", x, y);
    }
    return 0;
}