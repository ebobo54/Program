#include <stdio.h>
#include <math.h>
#include <unistd.h>

int main()
{

    double y,s,x = 0;
    printf("Enter number-> ");
    scanf("%lf", &s);
    int n;
    n=2/s+1;

    while(n)
    {
        if (x >= 0 && x <= 1)
            y = cos(x + pow(x, 3));
        if (x > 1 && x <= 2)
            y = exp(-pow(x, 2) - pow(x, 2) + 2 * x);
        printf("%lf %lf\n", x, y);
        x += s;
        n = n - 1;
    }
    return 0;
}