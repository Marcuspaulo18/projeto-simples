#include <stdio.h>

// Funçao para calcular o fatorial de um número inteiro
unsigned long long calcularFatorial(int num) {
    if (num == 0 || num == 1) {
        return 1; // Retorna 1 para casos base (fatorial de 0 e 1 eh 1)
    } else {
        unsigned long long fatorial = 1; // Inicializa o fatorial como 1
        for (int i = 2; i <= num; ++i) {
            fatorial *= i; // Multiplica fatorial por cada número de 2 ateh num
        }
        return fatorial; // Retorna o resultado do fatorial
    }
}

int main() {
    int numero;
    printf("Digite um número para calcular o fatorial: ");
    scanf("%d", &numero);

    if (numero < 0) {
        printf("O fatorial de numeros negativos nao eh definido.\n");
    } else {
        // Chama a funçao para calcular o fatorial
        unsigned long long resultado = calcularFatorial(numero);
        // Exibe o resultado do cálculo do fatorial
        printf("O fatorial de %d eh: %llu\n", numero, resultado);
    }

    return 0;
}