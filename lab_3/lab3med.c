#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]) {
    int i;
    for (i = 0; i < n; i++)
        a[i] = rand() % 101 - 50;
}

int findMinIndex(int n, int a[]) {
    int minIndex = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] < a[minIndex])
            minIndex = i;
    }
    return minIndex;
}

int findMaxIndex(int n, int a[]) {
    int maxIndex = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[maxIndex])
            maxIndex = i;
    }
    return maxIndex;
}

void process(int n, int a[]) {
    int minIndex = findMinIndex(n, a);
    int maxIndex = findMaxIndex(n, a);

    int sumIndex = minIndex + maxIndex;

    if (abs(sumIndex) < abs(minIndex)) {
        a[minIndex] = sumIndex;
    } else if (abs(sumIndex) > abs(maxIndex)) {
        a[maxIndex] = sumIndex;
    } else {
        int start = (minIndex < maxIndex) ? minIndex : maxIndex;
        int end = (minIndex > maxIndex) ? minIndex : maxIndex;

        for (int i = start + 1; i < end; i++) {
            a[i] = 0;
        }
    }
}

int main() {
    srand(time(NULL));
    int n;
    printf("n -> ");
    scanf("%d", &n);

    int *A = (int *)malloc(n * sizeof(int));

    if (A == NULL) {
        printf("Ошибка выделения памяти.\n");
        return 1;
    }

    fill(n, A);


    free(A);

    return 0;
}
