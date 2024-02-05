    #include <stdio.h>
    #include <stdbool.h>
    #include <math.h>
//bibliotecas//
    int main() {
      //declarando variaveis//
      int num, somapar = 0, prodimpar = 1, somatotal = 0;
      //iniciando o loop//
      while (1)
      {
        printf("Insira um numero inteiro positivo(ou 0 para encerrar):");
        scanf("%d", &num);

      //verifica se o numero é nulo para encerrar//
      if (num == 0)
      {
        break;
      }
      // Atualiza o contador de soma total//
      somatotal += num;
      // Verifica se o numero é par ou impar e modifica os contadores//
     if (num % 2 == 0)
     {
      somapar += num;
     }
     else
     {
      prodimpar *= num;
     }
      }
      //exibe na tela os valores dos contadores apos o encerramento//
      printf("A soma dos Numeros pares eh: %d\n", somapar);
      printf("O produto dos Numeros Impares eh: %d\n", prodimpar);
      printf("A soma de Todos os numeros lidos eh: %d\n", somatotal);

      return 0;
    }