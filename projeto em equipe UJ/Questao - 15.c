#include <stdio.h>
#include <stdlib.h>

int main() {
    double media;
    double soma_lidos=0;
    int quant_lidos=0;
    int soma_quadrado=0;
    long long produto_cubo = 1;
    int maiores_duzentos[100];

    printf("Digite um numero por vez. Digite 0 para terminar.\n");

    int input;
    int maiores_tamanho=0; //Quantos numeros há na array "maiores_duzentos"

    while (1) { //Loop para calcular a soma dos quadrados e produto dos cubos, assim como guardar os numeros maiores que 200.
        printf("Digite um numero: ");
        scanf("%d", &input);

        if (input == 0) {
            break;
        }

        if (maiores_tamanho < 100 && input > 200) { 
            maiores_duzentos[maiores_tamanho] = input;
            maiores_tamanho++;
        }


        soma_lidos+=input;
        quant_lidos++;
        soma_quadrado+=(input*input);
        produto_cubo *= (long long)(input*input*input);

    }
    media = soma_lidos/quant_lidos;

    
    printf("\n");
    printf("A media eh: %.2f", media);
    printf("\n");
    printf("A soma dos quadrados eh: %d", soma_quadrado);
    printf("\n");
    printf("O produto dos cubos eh: %lld", produto_cubo);
    printf("\n");
    printf("Os numeros digitados maiores que 200 foram: ");                        
    for (int j = 0; j < maiores_tamanho; j++) {
        printf("%d ", maiores_duzentos[j]);
    }
    
    return 0;
}