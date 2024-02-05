#include <stdio.h>		// Inclui a biblioteca padrao de entrada/saida para usar funcoes como printf e scanf.

 int
main ()
{				// Incio da funcao principal.
  int numeros[100];		// Declara um array de inteiros com espaço para 100 numeros.
  int i = 0;			// Inicializa uma variavel para contar quantos numeros foram lidos.
  int numero;			// Declara uma variavel para armazenar cada nC:mero lido.
  
printf ("Digite uma sequencia de numeros (0 para finalizar):\n");	// Imprime uma mensagem pedindo ao usuC!rio que insira nC:meros.
  
  do
    {
      
scanf ("%d", &numero);	// LC* um nC:mero da entrada padrC#o (teclado) e armazena na variC!vel 'numero'.
      
if (numero != 0)
	{			// Verifica se o nC:mero lido C) diferente de zero.
	  numeros[i] = numero;	// Armazena o nC:mero no array 'numeros'.
	  i++;			// Incrementa o contador 'i' para acompanhar quantos nC:meros foram lidos.
	}
    
}
  while (numero != 0);		// Continua lendo nC:meros atC) que o nC:mero zero seja inserido.
  
printf ("Numeros em ordem crescente:\n");	// Imprime uma mensagem indicando que a lista de nC:meros serC! exibida em ordem crescente.
  
    // Loop para imprimir os nC:meros em ordem crescente.
    for (int j = 0; j < i; j++)
    {
      
printf ("%d ", numeros[j]);	// Imprime cada nC:mero do array 'numeros'.
    } 
 
printf ("\nNumeros em ordem decrescente:\n");	// Imprime uma mensagem indicando que a lista de nC:meros serC! exibida em ordem decrescente.
  
    // Loop para imprimir os nC:meros em ordem decrescente.
    for (int j = i - 1; j >= 0; j--)
    {
      
printf ("%d ", numeros[j]);	// Imprime cada nC:mero do array 'numeros' em ordem decrescente.
    } 
 
return 0;		// Retorna 0 para indicar que o programa foi concluC-do com sucesso.
}


