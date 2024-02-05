#include <stdio.h>

int main() {
    int numeros[100]; // Declara um array para armazenar os numeros
    int tamanho = 0; // Variável para rastrear o número de elementos
    int numero, soma = 0;

    printf("Digite uma sequencia de numeros (digite 0 para encerrar):\n");

    // Lê os numeros até encontrar um número zero
    do {
        scanf("%d", &numero);
        if (numero != 0) {
            numeros[tamanho] = numero;
            soma += numero; // Calcula a soma dos numeros
            tamanho++;
        }
    } while (numero != 0);

    if (tamanho == 0) {
        printf("Nenhum numero foi inserido.\n");
        return 0;
    }

    // Calcula a média dos numeros
    float media = (float)soma / tamanho;

    printf("\nSoma de cada numero com a media:\n");
    for (int i = 0; i < tamanho; ++i) {
        float resultado = numeros[i] + media; // Soma o número com a média
        printf("%d + Media (%.2f) = %.2f\n", numeros[i], media, resultado);
    }

    return 0;
}