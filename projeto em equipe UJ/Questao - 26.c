//bibliotecas
#include <stdio.h>
#include <math.h>

int main() {
//variáveis
    int n;
    float s;
//condição para loop
    for (n = 10; n <= 1000; n += 10) {
    //calculo
        s = pow (1.0 + 1.0 / n, n);
        //resposta 
        printf("n = %d, s = %f \n", n, s);
    }

    return 0;
}