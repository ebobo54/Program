#include <stdio.h>
#include <math.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

int main()
{
    double y, s, x = 0;
    printf("Enter step size -> ");
    scanf("%lf", &s);
    int n;
    int k;
    k = 0;
    n = 2 / s;

    // Указать путь к исполняемому файлу gnuplot
    FILE *gnuplotPipe = popen("\"D:\\GitHub\\gnuplot\\bin\\gnuplot.exe\" -persist", "w");

    // Остальной код остается неизменным
    // ...

    pclose(gnuplotPipe);

    return 0;
}
