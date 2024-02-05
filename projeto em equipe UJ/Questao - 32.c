#include <stdio.h>

int main(void) {
    int par[10], impar[10], pares = 0, impares = 0, num;
    int i;
    float num_read;

    while (1) {
        printf("Digite um numero qualquer (0 para sair): ");
        if (scanf("%f", &num_read) != 1 || num_read != (int)num_read || num_read < 0) {
            printf("Desculpe, mas so aceitamos numeros inteiros positivos. \n");
        } else {
            num = (int)num_read;

            if (num == 0) {
                break; // Se o numero digitado for zero, saia do loop.
            }

            if (num & 1) {
                // Se o numero for ímpar, armazene-o no array 'impar'.
                impar[impares++] = num;
            } else {
                // Se o numero for par, armazene-o no array 'par'.
                par[pares++] = num;
            }
        }
    }

    printf("Total de numeros pares: %d\n", pares);
    for (i = 0; i < pares; i++) {
        printf("par[%d] = %d\n", i, par[i]); // Exibe os numeros pares e seus índices no array 'par'.
    }

    printf("Total de numeros impares: %d\n", impares);
    for (i = 0; i < impares; i++) {
        printf("impar[%d] = %d\n", i, impar[i]); // Exibe os numeros ímpares e seus índices no array 'impar'.
    }

    return 0;
}
