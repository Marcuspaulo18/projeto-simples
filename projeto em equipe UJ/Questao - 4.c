#include<stdio.h>

int main();
int contador;
int isPrime(int num) {
    if (num <= 1) {
        return 0;  
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0; 
        }
    }

    return 1;  
}

int main() {
    int num;

    do {
        printf("Insira um numero: (0 para encerrar): ");
        scanf("%d", &num);

        if (num != 0) {
            if (isPrime(num)) {
                printf("%d Eh um numero primo.\n", num);
                contador++;
            } else {
                printf("%d Nao eh um numero primo.\n", num);
            }
        }
    } while (num != 0);
    printf("%d  numeros primos", contador);

    return 0;
}