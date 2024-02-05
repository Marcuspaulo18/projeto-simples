#include<stdio.h>

int numero;
int soma;
int produto=1;

int main() {

    do{
        printf("Digite um numero:");
        scanf("%d", &numero);

        if (numero==0) {
            printf("Soma dos numeros: %d \n", soma);
            printf("Produto dos numeros: %d", produto);
            break;
        }
        
        if( numero > 2 && numero < 100 && numero != 10 && numero != 20 && numero != 32)
        {
         soma += numero;
        produto *= numero;
        }
     
    }while(numero!=0);

return 0;
}