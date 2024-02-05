#include <stdio.h>

int main() {
    double valor1, valor2, resultado;
    char operador;

    // Solicita ao usuário que insira os valores e o operador
    printf("Digite o primeiro valor: ");
    scanf("%lf", &valor1);

    printf("Digite o operador (+, -, , /): ");
    scanf(" %c", &operador);

    printf("Digite o segundo valor: ");
    scanf("%lf", &valor2);

    // Realiza a operação com base no operador inserido
    switch (operador) {
        case '+':
            resultado = valor1 + valor2;
            break;
        case '-':
            resultado = valor1 - valor2;
            break;
        case 'x':
            resultado = valor1 * valor2;
            break;
        case '/':
            if (valor2 != 0) {
                resultado = valor1 / valor2;
            } else {
                printf("Erro: divisão por zero\n");
                return 1; // Saída com código de erro
            }
            break;
        default:
            printf("Operador inválido\n");
            return 1; // Saída com código de erro
    }

    // Imprime o resultado da expressão
    printf("Resultado: %.2lf\n", resultado);

    return 0; // Saída bem-sucedida
}