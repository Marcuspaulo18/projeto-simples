#include <stdio.h>

int main()
{
//declaração  de variáveis 
    int numero;
    int soma= 0;
    int produto=1;
 
    do {
//entrada e  leitura dos dados
        printf("Digite um numero (0 para encerrar):");
        scanf("%d", &numero);

//verifica se o número é diferente de 0 para dar continuidade 
      if (numero != 0)
    {
        produto *= numero;
        soma += numero * numero; // Calcula o quadrado diretamente
    }

    }while(numero != 0);
    
//Exibição  do resultado 
    printf("O produto dos numeros: %d \n", produto);
    printf("A soma dos quadrados dos numeros: %d", soma);

    return 0;
}