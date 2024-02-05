#include <stdio.h>
#include <stdlib.h>

int opcpag (){
    int opcoes;
    
    printf ("\nOpçoes de pagamento:\n");
    printf ("1 - A vista com 10%% de desconto\n");
    printf ("2 - Dividido em 2x baseado no preço da etiqueta\n");
    printf ("3 - De 3x a 10x com 3%% de juros ao mes (somente acima de R$100)");
    
    printf ("digite a opçao desejada: ");
    scanf ("%d", &opcoes);
    
    return opcoes;
}

void calcprest (float total) {
    int parcelas;
    float valorparcelas;
    
    switch (opcpag()) {
        case 1:
            total *= 0.9;
            printf ("\n Total a pagar (a vista com 10%% de desconto): R$%.2f\n", total);
            break;
        case 2:
            valorparcelas = total / 2.0;
            printf ("\nTotal a pagar (dividido em 2x): R$%.2f em duas parcelas de R$%.2f\n", total, valorparcelas);
            break;
        case 3:
            if (total > 100) {
                printf ("digite o numero de parcelas (3 a 10): ");
                scanf ("%d", &parcelas);
                
                if (parcelas >= 3 && parcelas <= 10) {
                    valorparcelas = (total * 1.03) / parcelas;
                    printf ("\ntotal a pagar (em %d vezes com 3%% de juros ao mes): R$%.2f em %d parcelas de R$%.2f\n", parcelas, total * 1.03, parcelas, valorparcelas);
                } else {
                    printf ("numero de parcelas invalido. \n");
                }
            } else {
                printf ("Opcao indisponivel para compras abaixo de R$ 100");
            }
            break;
        default:
            printf ("Opcao invalida. \n");
    }
}

int main() {
    float total;
    
    printf ("digite o total gasto pelo cliente: R$");
    scanf ("%f", &total);
    
    calcprest(total);
    
    return 0;
}
