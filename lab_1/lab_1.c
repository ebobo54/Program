#include <stdio.h>

int main()
{
    int amnam(int num)
    {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    int a, b, q, w;
    printf("Enter numbers a: ");
    scanf("%d", &a);
    printf("Enter numbers b: ");
    scanf("%d", &b);
    q = amnam(a);
    w = amnam(b);
    if (q > w) {
        printf("sum numbers a > sum numbers b %d\n", q);
    } if (q == w) {
        printf("Sum numbers = b %d\n", w);
    } if (q < w){
        printf("sum numbers a < b %d\n", q + w);
    }

    return 0;
}
