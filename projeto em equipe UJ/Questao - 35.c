#include <stdio.h>
#include <stdlib.h>
#include <time.h>

 void
embaralhar (int vetor[], int tamanho)
{
  
srand ((unsigned int) time (NULL));
  
 
for (int i = tamanho - 1; i > 0; i--)
    {
      
int j = rand () % (i + 1);
      
 
	// Troca os elementos i e j
      int temp = vetor[i];
      
vetor[i] = vetor[j];
      
vetor[j] = temp;

} 
} 
 
int

main ()
{
  
const int tamanho = 52;
  
int vetor[tamanho];
  
 
    // Inicializa o vetor com valores de 0 a 51
    for (int i = 0; i < tamanho; i++)
    {
      
vetor[i] = i;
    
} 
 
embaralhar (vetor, tamanho);
  
 
    // Imprime o vetor embaralhado
    for (int i = 0; i < tamanho; i++)
    {
      
printf ("%d ", vetor[i]);
    
} 
 
return 0;

}
