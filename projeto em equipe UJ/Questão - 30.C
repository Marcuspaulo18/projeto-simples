#include <stdio.h>

int main() {
    int resultado = 0; // Variável para armazenar o resultado das operações.
    int valor; // Variável para armazenar o valor a ser operado.
    char instrucao; // Variável para armazenar a instrução (operador).

    printf("Bem vindo ao interpretador de linguagem de programacao\n");
    printf("DICA RAPIDA!\nOs comandos do sistema podem ser executados por meio dos sinais:\n");
    printf("+(soma), -(subtracao), *(produto), /(divisao), s (sair do programa), = (executar a operacao)\n");
    printf("Logo mais aproveite a experiencia\n");

    while (1) {
        printf("Digite uma instrucao:\n");
        scanf(" %c", &instrucao); // Lê a instrução do usuário.

        if (instrucao == '=') {
            // Quando o usuário digita '=', exibe o valor atual de 'resultado'.
            printf("O valor eh: %d\n", resultado);
            continue;
        }
        if (instrucao == 's') {
            // Se o usuário digitar 's', sai do programa.
            printf("Saindo do programa...\n");
            break;
        }

        printf("Digite um valor:\n");
        scanf("%d", &valor); // Lê o valor a ser operado.

        // Usa um switch para determinar qual operação realizar com base na instrução.
        switch (instrucao) {
            case '+':
                resultado += valor; // Soma 'valor' a 'resultado'.
                break;
            case '-':
                resultado -= valor; // Subtrai 'valor' de 'resultado'.
                break;
            case '*':
                resultado *= valor; // Multiplica 'resultado' por 'valor'.
                break;
            case '/':
                if (valor != 0) {
                    resultado /= valor; // Divide 'resultado' por 'valor' (se 'valor' não for zero).
                } else {
                    printf("Nao se pode dividir por zero\n");
                }
                break;
            default:
                printf("Instrucao invalida\n"); // Se a instrução não for reconhecida.
                break;
        }
    }
    return 0;
}
