#include <stdio.h>
#include <math.h>
#include <unistd.h>

int main()
{

    double y,s,x = 0;
    printf("Enter number-> ");
    scanf("%lf", &s);
    int n;
    int k;
    k = 0;
    n = 2 / s;

    while(n >= k)
    {
        if (x >= 0 && x <= 1)
            y = cos(x + pow(x, 3));
        if (x > 1 && x <= 2)
            y = exp(-x*x) - (x*x) + 2 * x;
        printf("%lf %lf\n", x, y);
        x += s;
        k++;
    }
    return 0;
}