#include <stdio.h>
#include <math.h>

int main() {
    int rmaior5menor10 = 0;
    int rmenor2 = 0;
    int rcomplexas = 0;
    double a, b, c;
    double d, x1, x2;
    double sx, px = 0;

    while (1) {
        // Solicita e lê os valores de a, b e c para a equação de segundo grau
        printf("Informe os valores de a, b e c:");
        scanf("%lf %lf %lf", &a, &b, &c);

        // Se 'a' for zero, encerra o loop e finaliza o programa
        if (a == 0) {
            break;
        }

        // Calcula o delta da equação de segundo grau
        d = (b*b)-(4*a*c);

        if (d > 0) {
            // Se o delta é maior que zero, há duas raízes reais
             x1 = ((-b) + sqrt(d)) / (2 * a);
             x2 = ((-b) - sqrt(d)) / (2 * a);
                printf("As raizes sao:%.2lf ", x1);
                printf("e %.2lf\n", x2);

            if (x1 > 5 && x1 < 10 && x2 > 5 && x2 < 10) {
                // Verifica se as raízes estão entre 5 e 10 e atualiza o contador
                rmaior5menor10 += 2;
                sx = x1 + x2;
                printf("A soma das Raizes eh: %lf\n", sx);
            } else if (x1 < 2 && x2 < 2) {
                // Verifica se as raízes são menores que 2 e atualiza o contador
                px = x1 * x2;
                rmenor2 += 2;
                printf("O produto das Raizes eh: %lf\n", px);
            }
        } else if  (d < 0) {
            // Se o delta é menor que zero, há duas raízes complexas
            rcomplexas += 2;
            printf("Raizes complexas\n");
        }
    }

    // Imprime a quantidade de raízes que satisfazem as condições
    printf("Quantidade de Raizes Menores que 2 Lidas: %d\n", rmenor2);
    printf("Quantidade de Raizes maiores que 5 e Menores que 10 Lidas: %d\n", rmaior5menor10);
    printf("Quantidade de Raizes Complexas Lidas: %d\n", rcomplexas);

    return 0;
}
