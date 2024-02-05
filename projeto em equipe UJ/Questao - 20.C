#include <stdio.h>
#include <stdlib.h>

int main (){
    int n, i = 0;
    int num [100];
    
    printf ("insira uma sequencia de numeros (0 para encerrar): ");
    do {
        scanf ("%d",&n);
        
        if (n !=0) {
            num[i] = n;
            i++;
        }
    } while (n !=0 && i < 100);
    
    printf ("\nsua sequencia na ordem inversa: ");
    for (int f = i - 1; f >= 0; f--) {
        printf("%d ", num[f]);
    }
    return 0;
}