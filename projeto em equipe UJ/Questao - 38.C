#include <stdio.h>

#define TAMANHO 3 // Tamanho da matriz tridimensional

int main() {
    int matriz[TAMANHO][TAMANHO][TAMANHO]; // Declaração da matriz tridimensional
    int somaArestas = 0;

    printf("Preencha a matriz tridimensional %dx%dx%d:\n", TAMANHO, TAMANHO, TAMANHO);

    // Preenchimento da matriz tridimensional
    for (int i = 1; i <= TAMANHO; ++i) {
        for (int j = 1; j <= TAMANHO; ++j) {
            for (int k = 1; k <= TAMANHO; ++k) {
                printf("Digite o valor para matriz[%d][%d][%d]: ", i, j, k);
                scanf("%d", &matriz[i - 1][j - 1][k - 1]);
            }
        }
    }

    printf("\nDiagonal principal da matriz tridimensional:\n");
    for (int i = 0; i < TAMANHO; ++i) {
        printf("%d ", matriz[i][i][i]); // Imprime os elementos da diagonal principal
    }
    printf("\n");

    // Soma dos elementos das arestas da matriz tridimensional
    for (int i = 0; i < TAMANHO; ++i) {
        for (int j = 0; j < TAMANHO; ++j) {
            for (int k = 0; k < TAMANHO; ++k) {
                if (i == 0 || j == 0 || k == 0 || i == TAMANHO - 1 || j == TAMANHO - 1 || k == TAMANHO - 1) {
                    somaArestas += matriz[i][j][k]; // Soma elementos das arestas
                }
            }
        }
    }

    printf("\nSoma dos elementos das arestas: %d\n", somaArestas);

    return 0;
}