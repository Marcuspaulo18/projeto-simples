#include <stdio.h>
#include <limits.h>

int main() {
    int numero;
    int menor = INT_MAX;
    int soma = 0;
    int produto = 1;

    printf("Digite um numero (0 para sair): ");
    scanf("%d", &numero);

    while (numero != 0) {
        if (numero < menor) {
            menor = numero;
        }

        if (numero > 10) {
            soma += numero;
        }

        if (numero > 200) {
            produto *= numero;
        }

        printf("Digite um numero (0 para sair): ");
        scanf("%d", &numero);
    }

    printf("Menor numero lido: %d\n", menor);
    printf("Soma dos numeros maiores que 10: %d\n", soma);
    printf("Produto dos numeros maiores que 200: %d\n", produto);

    return 0;
}