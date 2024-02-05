//biblioteca
#include <stdio.h>
#include <math.h>

//declaração de variáveis
int num;
int soma_a = 0;
int produto_b = 1;
int somamedia;
float media = 0;
int produto_d = 1;
int soma_e = 0;
int contador = 0;

int main() {

    printf("Insira um numero ( 0, 14 ou 99 para encerrar): \n");

    do {

//leitura dos dados
        scanf("%d", &num);

//verifica as condições para prosseguir
        if ( num != 0 && num != 99 && num != 14 ) {

            //operação  da média
            somamedia += num;
            contador ++;
            media = somamedia / contador;

//condições pedidas na questão
            if ( num > 50 && num < 150 )
            {
                soma_a += num;
            }
            if ( num != 10 && num > 5 && num < 70 )
            {
                produto_b *= num;
            }
            if  ( num > 20 && num < 30 )
            {
                produto_d *= num;
            }
            if  ( num > 16 )
            {
                soma_e += pow(num, 2);
            }
        }
    } while ( num != 0 && num != 99 && num != 14);

    //mostra o resultado na tela
    printf(" a soma dos numeros lidos menores do que 150 e maiores do que 50 eh:) %d \n", soma_a );
    printf(" o produto dos numeros lidos que sejam concomitantemente diferentes de 10, maiores do que 5 e menores do que 70 eh:) %d \n", produto_b);
    printf(" a media dos numeros lidos eh:) %.1f \n", media);
    printf(" o produto dos numeros lidos maiores do que 20 e menores do que 30 eh:) %d \n", produto_d);
    printf(" a soma dos quadrados dos numeros lidos maiores do que 16 eh:) %d \n", soma_e);

    return 0;
}