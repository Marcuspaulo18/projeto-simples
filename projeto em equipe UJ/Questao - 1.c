#include <stdio.h>
void checkNumber() {
    int numero, numerolido=0;
    int maiorque100 = 0;
    int  menorque10 = 0;
    int  iguala20= 0;
    int iguala30= 0;
    int iguala40= 0;

    while (1) {
        printf("Digite  um numero (0 para terminar o programa): ");
        scanf("%d", &numero);

        if (numero == 0) {
            printf("Quantidade de numeros lidos:%d\n",numerolido);
            printf("Maiores que 100: %d\n", maiorque100);
            printf("Menores que 10: %d\n", menorque10);
            printf("Iguais a 20: %d\n", iguala20);
            printf("Iguais a 30: %d\n", iguala30);
            printf("Iguais a 40: %d\n", iguala40);
            break;
        }

        if (numero > 100) {
            maiorque100++;
            numerolido++;
            printf("numero eh maior que 100.\n");
        } else if (numero < 10) {
            menorque10++;
            numerolido++;
            printf("numero eh menor que 10.\n");
        } else if (numero == 20) {
            iguala20++;
            numerolido++;
            printf("numero eh igual a 20.\n");
        } else if (numero == 30) {
            iguala30++;
            numerolido++;
            printf("numero eh igual a 30.\n");
        } else if (numero == 40) {
            iguala40++;
            numerolido++;
            printf("numero eh igual a 40.\n");
        } else {
            printf("numero nao entra em alguma condicao.\n");
        }
    }
}

int main() {
    checkNumber();
    return 0;
}



