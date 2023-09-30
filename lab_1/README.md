# lab_1
 
 ---

 ## Задание
Вывести сумму цифр числа a если она больше b, если равна b - сообщение Сумма цифр = b, и значение суммы, увеличенное на b, если сумма меньше b.
```c
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
```
![](Q.png)
## Результаты работы

---

a>b
![](W.png)

---

a=b
![](R.png)

---

a<b
![](E.png)

---
```mermaid
flowchart TD
A[Начало] --> B{a,b};
B ----> C[a>b];
C -- true --> D[print a];
C -- false --> E[a=b];
E -- true --> F[Сумма цифр = b];
E -- false --> G[b>a];
G ----> H[a+b];
H ----> I[Конец];
D ----> I[Конец];
F ----> I[Конец];
```
1. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
2. [stackoverflow](https://stackoverflow.com/questions/34836305/how-do-i-make-a-flowchart-using-markdown-on-my-github-blog)