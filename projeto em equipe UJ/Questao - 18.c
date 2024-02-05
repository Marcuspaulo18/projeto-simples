#include <stdio.h>
#include <math.h>

int main() {
    int n_i = 6;
    int n_k = 7;
    int i = 1;
    int k = 3;
    double resultado = 0.0;

    while (i <= n_i) {                 //Calcula o somatório
        k = 3;
        while (k <= n_k) {
            resultado += (pow(2, (3 * i + k)) / (i * k + 1)) * k; //pow(2, ( X )) 2 será a base e X o expoente
            k++;
        }
        i++;
    }

    printf("%lf\n", resultado);
    return 0;
}