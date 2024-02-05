#include <stdio.h>

int main (){
    int matriz[3][3];
    int somadiagonalsecundaria = 0;
//leitura dos elementos da matriz - inicio//
    printf ("digite os elementos da matriz: ");
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            printf ("digite o elemento da linha [%d] e coluna [%d]: ", i + 1, j + 1);
            scanf ("%d", &matriz[i][j]);
        }
    }
//leitura dos elementos da matriz - fim//
//impressão da matriz sem a diagonal - inicio//
    printf ("elementos da matriz (exceto diagonal principal): \n");
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (i != j){
                printf("%d", matriz[i][j]);
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
//impressão da matriz sem a diagonal - fim//
//calculo dos elementos - inicio//
    for (int i = 0;  i < 3; i++){
        somadiagonalsecundaria  += matriz[i][2 - i];
    }
    
    printf ("a soma dos elementos da diagonal secundaria é: %d\n", somadiagonalsecundaria);
    return 0;
}
//calculo dos elementos - fim//