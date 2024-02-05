#include <stdio.h>

// Função para ordenar em ordem crescente usando o algoritmo de Bubble Sort
void ordenarCrescente(int array[], int tamanho) {
    int i, j, temp;
    for (i = 0; i < tamanho - 1; ++i) {
        for (j = 0; j < tamanho - 1 - i; ++j) {
            if (array[j] > array[j + 1]) {
                // Troca os elementos se estiverem fora de ordem
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

// Função para ordenar em ordem decrescente usando o algoritmo de Bubble Sort
void ordenarDecrescente(int array[], int tamanho) {
    int i, j, temp;
    for (i = 0; i < tamanho - 1; ++i) {
        for (j = 0; j < tamanho - 1 - i; ++j) {
            if (array[j] < array[j + 1]) {
                // Troca os elementos se estiverem fora de ordem
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

int main() {
    int numeros[100];
    int tamanho = 0;
    int i, temp;

    printf("Digite uma sequência de números (digite 0 para encerrar):\n");

    // Lê os números até encontrar um número zero
    do {
        scanf("%d", &temp);
        if (temp != 0) {
            numeros[tamanho] = temp;
            tamanho++;
        }
    } while (temp != 0);

    // Ordena em ordem crescente
    ordenarCrescente(numeros, tamanho);
    printf("\nNúmeros em ordem crescente:\n");
    for (i = 0; i < tamanho; ++i) {
        printf("%d ", numeros[i]);
    }

    // Ordena em ordem decrescente
    ordenarDecrescente(numeros, tamanho);
    printf("\n\nNúmeros em ordem decrescente:\n");
    for (i = 0; i < tamanho; ++i) {
        printf("%d ", numeros[i]);
    }

    return 0;
}