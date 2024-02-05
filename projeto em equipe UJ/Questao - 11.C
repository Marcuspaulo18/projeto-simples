#include <stdio.h>
#include <string.h>
#include <math.h>
//bibliotecas//

int main() {
  
  //declarando variavel//
  int num;
  //iniciando loop//
  while (1)
  {
  //solicita o número e armazena//
  printf("\nDigite um numero inteiro positivo(ou 0 para encerrar):\n");
  scanf("%d",&num);
  // condição para encerrar o programa
  if(num ==0)
  {
    printf("\nFinalizando programa!\n");
    break;
  }
  //verificando se o numero lido é par ou impar//
  if (num % 2 == 0)
  {
   printf("\nO numero informado eh par\n");
  
  }
  else {
  printf("\nO numero informado eh impar\n");
  }
  }
  return(0);
}