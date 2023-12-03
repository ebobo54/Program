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

    FILE *gnuplotPipe = popen("gnuplot -persist", "w");

    fprintf(gnuplotPipe, "set terminal gif animate delay 50\n");
    fprintf(gnuplotPipe, "set output 'animation.gif'\n");
    fprintf(gnuplotPipe, "set xlabel 'X'\n");
    fprintf(gnuplotPipe, "set ylabel 'Y'\n");
    fprintf(gnuplotPipe, "set xrange [0:2]\n");
    fprintf(gnuplotPipe, "set yrange [-2:2]\n");

    fprintf(gnuplotPipe, "do for [i=1:%d] {\n", n);
    fprintf(gnuplotPipe, "    plot '-' with lines title 'Step '.i\n");

    while (n >= k)
    {
        if (x >= 0 && x <= 1)
            y = cos(x + pow(x, 3));
        if (x > 1 && x <= 2)
            y = exp(-x * x) - (x * x) + 2 * x;
        fprintf(gnuplotPipe, "%lf %lf\n", x, y);
        fflush(gnuplotPipe);
        x += s;
        k++;

#ifdef _WIN32
        Sleep(50); // Пауза в миллисекундах (50 миллисекунд) для анимации
#else
        usleep(50000); // Пауза в микросекундах (50 миллисекунд) для анимации
#endif
    }

    fprintf(gnuplotPipe, "    e\n");
    fprintf(gnuplotPipe, "}\n");

    pclose(gnuplotPipe);

    return 0;
}
