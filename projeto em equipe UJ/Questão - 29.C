#include <stdio.h>
#include <string.h>

// Declaração de variáveis para nome, rua, telefone e idade, usando arrays de caracteres.
char nome[100], rua[100], tel[15];
int idade;

int main() {
    printf("/////LOCALIZADOR/////\n"); // Título do programa.
    printf("Qual eh o seu nome?\n");

    // Usando fgets() para ler uma linha de texto (incluindo espaços) e armazená-la na variável 'nome'.
    fgets(nome, sizeof(nome), stdin);
    
    // Removendo o caractere de nova linha ('\n') da entrada.
    nome[strcspn(nome, "\n")] = '\0';  

    printf("Qual eh a sua idade?\n");

    // Usando scanf() para ler um número inteiro e armazená-lo na variável 'idade'.
    scanf("%d", &idade);

    // Limpar o buffer de entrada após a leitura do número inteiro.
    while (getchar() != '\n');

    printf("Em qual rua voce mora?\n");

    // Usando fgets() para ler o nome da rua e armazená-lo na variável 'rua'.
    fgets(rua, sizeof(rua), stdin);
    
    // Removendo o caractere de nova linha ('\n') da entrada.
    rua[strcspn(rua, "\n")] = '\0';  

    printf("Poderia me dar o numero do seu telefone?\n");

    // Usando fgets() para ler o número de telefone e armazená-lo na variável 'tel'.
    fgets(tel, sizeof(tel), stdin);
    
    // Removendo o caractere de nova linha ('\n') da entrada.
    tel[strcspn(tel, "\n")] = '\0';  

    // Impressão das informações coletadas.
    printf("Seu nome eh %s, voce tem %d anos, voce mora na rua %s e seu telefone eh %s\n", nome, idade, rua, tel);

    return 0;
}
