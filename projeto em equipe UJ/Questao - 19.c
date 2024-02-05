#include <stdio.h>
#include <math.h>

int main() {
    int n_j = 4;
    int n_i = 6;
    int n_k = 7;
    int j = 1;
    int i = 1;
    int k = 3;

    double resultado = 0;

    while (j <= n_j) {        //Calcula o somatório
        i = 1;
        while (i <= n_i) {
            k = 3;
            while (k <= n_k) {
                resultado += pow(2, j * i + k) / (i * k + 1) * (k * pow(j, i)); //pow(2, ( X )) 2 será a base e X o expoente
                k++;
            }
            i++;
        }
        j++;
    }

    printf("%lf\n", resultado);

    return 0;
}