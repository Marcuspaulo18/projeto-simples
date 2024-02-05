#include <stdio.h>
#include <math.h>

int main() {
    int n = 6;
    int i = 1;
    double resultado = 0.0;

    while (i <= n) {              //Calcula o somatório
    
        resultado += pow(2, (3 * i + i * i)) / (i + 1); // pow(2, ( X )) 2 será a base e X o expoente
        i++;
    }

    printf("%lf\n", resultado);
    return 0;
}