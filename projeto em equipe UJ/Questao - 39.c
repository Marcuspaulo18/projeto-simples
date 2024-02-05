#include<stdio.h>
#include<string.h>
int main()
{
char letra;
char frase[101];
int i, cont=0;
    printf("digite uma frase qualquer:");
    fgets(frase,sizeof(frase),stdin);
    printf("digite uma letra de sua escolha:");
    scanf("%c", &letra);
    int tamanho=strlen(frase);
    for(i=0;i<tamanho;i++){
    if(frase[i]==letra){
    cont++;
    }
    }
    printf("a letra %c aparece %d vezes na frase:\n%s",letra,cont,frase);
    return 0;
}