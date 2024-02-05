#include<stdio.h>

// Função para calcular a média de um array
float media(float unid[], int tam){
    float med, soma=0;
    int i;
    for(i=0; i<tam; i++){
        soma = soma + unid[i];
    }
    med = soma / tam;
    return med;
}

// Função para calcular a média ponderada de um array
float ponderada(float unid[], int tam){
    float med_pond, soma=0;
    int i;
    for(i=0; i<tam; i++){
        soma = soma + unid[i];
    }
    med_pond = (soma * 2) / tam;
    return med_pond;
}

// Função para encontrar o maior elemento em um array
float maioral(float unid[], int tam){
    float mai = unid[0]; 
    int i;
    for(i=0; i<tam; i++){
        if(unid[i] > mai){
            mai = unid[i];
        }
    }
    return mai;
}

// Função para encontrar números primos em um array e retorná-los em um novo array
int* primos(float unid[], int tam, int *num_primos){
    int *primos_array = malloc(tam * sizeof(int)); 
    int count = 0;
    
    for(int i=0; i<tam; i++){
        int primo = 1; 
        if(unid[i] > 1){
            for(int j=2; j<unid[i]; j++){
                if((int)unid[i] % j == 0){
                    primo = 0; 
                    break;
                }
            }
            if(primo == 1){
                primos_array[count++] = (int)unid[i];
            }
        }
    }
    
    *num_primos = count;
    return primos_array;
}

// Função para normalizar um array, dividindo cada elemento pelo maior elemento
void normalizando(float unid[], int tam){
    float mai = unid[0]; 
    int i;
    for(i=0; i<tam; i++){
        if(unid[i] > mai){
            mai = unid[i];
        }
    }
    for(i=0; i<tam; i++){
        if(unid[i] > mai){
            unid[i] = unid[i]/mai;
        }
    }
}

int main(){
    float med, med_pond, mai;
    int *primos_array, num_primos, normal;

    // Array de exemplo
    float array_unid[] = {2,4,35,50,23,17,9,12,27,5,14,2,3,4,1,2,5,6,8,9};
    
    // Calcular média, média ponderada e encontrar o maior elemento
    med = media(array_unid, 20);
    med_pond = ponderada(array_unid, 20);
    mai = maioral(array_unid, 20);
    
    // Encontrar números primos no array
    primos_array = primos(array_unid,20,&num_primos);
    
    // Imprimir resultados
    printf("A média do array será: %.2f\n", med);
    printf("A média ponderada do array será: %.2f\n", med_pond);
    printf("O maior valor do array será: %.2f\n", mai);
    printf("Os números primos do array são: ");
    for(int i = 0; i < num_primos; i++){
        printf("%d,", primos_array[i]);
    }
    printf("\n");
    
    // Liberar memória alocada para o array de números primos
    free(primos_array); 
    
    // Normalizar o array e imprimir os valores normalizados
    normal=normalizando(array_unid,20);
    printf("Vetor normalizado: ");
    for (int i = 0; i < 1; i++) {
        printf("%.2f ", array_unid[i]);
    }
    printf("\n");
    
    return 0;
}
