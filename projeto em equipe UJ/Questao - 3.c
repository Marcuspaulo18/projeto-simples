#include <stdio.h>

int main()
{
   int numero = 0;
   int soma= 0;
   int contador=0;
   
   do{
      printf("Digite um numero: (0 para encerrar)");
      scanf("%d", &numero);
      if(numero > 0)
      {
         soma=soma+numero;
         contador=contador+1;
      }
   }while(numero>0);
   
 printf("Resultado da soma: %d \n", soma);
 printf("Quantos numeros foram lidos: %d", contador);
   return 0;
}