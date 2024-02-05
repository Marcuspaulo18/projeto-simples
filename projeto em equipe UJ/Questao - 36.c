#include <stdio.h>

void smmatrizes(int A[5][5], int B[5][5], int final[5][5], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            final[i][j] = A[i][j] + B[i][j];
        }
    }
}

int smdiagonal(int mt[5][5], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += mt[i][i];
    }
    return soma;
}

void mpcmatrizes(int A[5][5], int B[5][5], int final[5][5], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            final[i][j] = 0;
            for (int k = 0; k < n; k++) {
                final[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void pressmatriz(int mt[5][5], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d\t", mt[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n;

    printf("Digite a dimensao das matrizes (max - 5): ");
    scanf("%d", &n);

    int A[5][5], B[5][5], sm[5][5], pdt[5][5];

    printf("Digite os elementos da primeira matriz (A):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    printf("Digite os elementos da segunda matriz (B):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    smmatrizes(A, B, sm, n);

    int smdiagonalA = smdiagonal(A, n);
    int smdiagonalB = smdiagonal(B, n);

    mpcmatrizes(A, B, pdt, n);

    printf("\nSoma das matrizes:\n");
    pressmatriz(sm, n);

    printf("\nSoma das diagonais da matriz A: %d\n", smdiagonalA);
    printf("Soma das diagonais da matriz B: %d\n", smdiagonalB);

    printf("\nProduto das matrizes:\n");
    pressmatriz(pdt, n);

    return 0;
}
