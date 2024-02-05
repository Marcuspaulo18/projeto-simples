#include <stdio.h>		// Inclui a biblioteca padrC#o de entrada/saC-da, que C) necessC!ria para usar funC'C5es como printf.

 int
main ()				// DeclaraC'C#o da funC'C#o principal, que C) onde a execuC'C#o do programa comeC'a.
{
  
printf ("Tabuada de 1 a 9:\n");	// Imprime uma mensagem na tela indicando o que o programa farC!.
  
    // Um loop for aninhado que calcula e imprime as tabuadas de multiplicaC'C#o.
    for (int i = 1; i <= 9; i++)	// Loop externo para as tabuadas de 1 a 9.
    {
      
printf ("Tabuada do %d:\n", i);	// Imprime a mensagem indicando qual tabuada estC! sendo exibida.
      
for (int j = 1; j <= 10; j++)	// Loop interno para multiplicar o nC:mero (i) de 1 a 10.
	{
	  
printf ("%d x %d = %d\n", i, j, i * j);	// Imprime o cC!lculo da multiplicaC'C#o.
	} 
 
printf ("\n");	// Imprime uma linha em branco para separar as tabuadas.
    } 
 
return 0;		// Retorna 0 para indicar que o programa foi concluC-do com sucesso.
}


