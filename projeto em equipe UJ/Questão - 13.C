//biblioteca//
#include <stdio.h>
//função principal//
int main() {
  // Inicializa a variável 'maior' com 0//
    int numero, maior = 0;  

    printf("Digite numeros: (insira 0 para finalizar):\n");
// Loop infinito//
    while (1) {  
        scanf("%d", &numero);
// Sai do loop quando o número for 0//
        if (numero == 0) {
            break;  
        }
// Atualiza a variavel 'maior' se um número maior for lido//
        if (numero > maior) {
            maior = numero;  
        }
    }

    if (maior != 0) {
        printf("O maior numero lido foi: %d\n", maior);
    } else {
        printf("Nenhum numero inserido.\n");
    }

    return 0;
}
