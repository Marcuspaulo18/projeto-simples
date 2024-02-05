#include <stdio.h>
#include <math.h>

int main() {
    
    int i = 1;
    int n = 6;
    double resultado = 0;

    while (i <= n) {   //Calcula o somatório

        resultado += (pow(i, (2 * i)) + exp(i) * i * sin(2 * i)); //pow(2, ( X )) 2 será a base e X o expoente
        i++;                         //"exp" é o Número de Euler, que é elevado a potência "i"
    }

    printf("%f\n", resultado);

    return 0;
}