# Lab_2
## Задание
![](Q.png)
### Описание проделанной работы
#### оператор цикла while 
```c
#include <stdio.h>
#include <math.h>
#include <unistd.h>

int main()
{

    double y,s,x = 0.0;
    printf("Enter number-> ");
    scanf("%lf", &s);
    int n;
    n=2/s+1;

    while(n)
    {
        if (x >= 0 && x <= 1)
            y = cos(x + pow(x, 3.0));
        if (x > 1 && x <= 2)
            y = exp(-pow(x, 2.0) - pow(x, 2.0) + 2.0 * x);
        printf("%lf %lf\n", x, y);
        x += s;
        n = n - 1;
    }
    return 0;
}
```
![](L2.png)

---
#### оператор цикла for
```c
#include <stdio.h>
#include <math.h>

int main()
{
    double y,s,x = 0.0;
    printf("Enter number-> ");
    scanf("%lf", &s);
    int n;
    n = s / 2.0;
    printf("x\t\ty\n");
    for(x = 0.0; x <= 2.0 + n; x = x + s)
    {
        if(x >= 0 && x <= 1)
            y = cos(x + pow(x, 3.0));
        else
            y = exp(-pow(x, 2.0) - pow(x, 2.0) + 2.0 * x);
        printf("%f\t%f\n", x, y);
    }
    return 0;
}
``````
![](L22.png)

---
### Результат
![](E.png)
___
### График функции
![](R.png)
---
### Блок-схема


```mermaid
graph TD;
    A[начало]-->B[x,y];
    B-->C[0≤x≤1];
    B-->D[1<x≤2];
    C-->E[cos(x+x^3)];
    D-->F[e^(-x^2)-x^2+2x];
    E-->G[x,y];
    F-->G;
    G-->Q[ x += s n = n - 1];
    Q --> W[Конец];
```


```mermaid
flowchart TD
    A[Начало] --> B{x,y};
    B --> C[?x?1];
    B --> D[1<x?2];
    C --> E[cos(x+x^3)];
    D --> F[e^(?x2)?x^2+2x];
    E --> G[x,y];
    F --> G[x,y];
    G --> Q[ x += s n = n - 1];
    Q --> W[Конец];
```