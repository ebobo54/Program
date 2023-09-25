#include <stdio.h>
int main()
{
    float a, b;
    printf("Enter a -> ");
    scanf("%f", &a);
    printf("Enter b -> ");
    scanf("%f", &b);
    if (a > b)
        printf("%f\n",a);
    if (a == b)
        printf("%f ë„¨¨† Ê®‰‡ =\n",b);
    if (a < b)
        printf("%f\n",a+b);
    return 0;

}

