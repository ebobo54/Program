#include <stdio.h>

int amnam(int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int main() {
    FILE *logFile;
    logFile = fopen("log.txt", "w");  

    if (logFile == NULL) {
        printf("Error opening log file.\n");
        return 1;
    }

    int a, b, q, w;

    do {
        printf("Enter numbers a (0 to exit): ");
        scanf("%d", &a);
        fprintf(logFile, "Input: a = %d\n", a);

        if (a == 0) {
            break;  
        }

        printf("Enter numbers b: ");
        scanf("%d", &b);
        fprintf(logFile, "Input: b = %d\n", b); 

        q = amnam(a);
        w = amnam(b);

        if (q > w) {
            printf("%d\n", q);
            fprintf(logFile, "Output: %d\n", q);  
        } else if (q == w) {
            printf("sum numbers = b %d\n", w);
            fprintf(logFile, "Output: sum numbers = b %d\n", w);  
        } else {
            printf("%d\n", q + w);
            fprintf(logFile, "Output: %d\n", q + w); 
        }
    } while (a != 0);

    fclose(logFile); 

    return 0;
}
