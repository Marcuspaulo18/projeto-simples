#include<stdio.h>

int main(void) {
    // Declaracao da matriz e variáveis
    float matriz[6][4];
    float soma = 0, media;
    int i, j;

    // Entrada de dados na matriz
    for(i = 1; i <= 5; i++) {
        for(j = 1; j <= 3; j++) {
            printf("Digite o valor para a posicao [%d] [%d]: ", i, j);
            scanf("%f", &matriz[i][j]);
            soma += matriz[i][j]; // Soma dos elementos da matriz
        }
    }

    // Cálculo das médias das colunas
    for(j = 1; j <= 3; j++) {
        media = 0;
        for(i = 1; i <= 5; i++) {
            media += matriz[i][j];
        }
        media /= 5;
        // Adicao da média à coluna correspondente
        for(i = 1; i <= 5; i++) {
            matriz[i][j] += media;
        }
    }

    // Impressão da matriz original
    printf("\nMatriz original:\n");
    for(i = 1; i <= 5; i++) {
        for(j = 1; j <= 3; j++) {
            printf("%.f ", matriz[i][j]);
        }
        printf("\n");
    }

    // Impressão da matriz transposta
    printf("\nMatriz transposta:\n");
    for(j = 1; j <= 3; j++) {
        for(i = 1; i <= 5; i++) {
            printf("%.f ", matriz[i][j]);
        }
        printf("\n");
    }

    // Impressão da soma de todos os elementos da matriz
    printf("\nSoma de todos os elementos: %.f\n", soma);

    return 0;
}
    