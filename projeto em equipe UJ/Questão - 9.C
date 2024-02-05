#include <stdio.h>
#include <string.h>
#include <math.h>
//bibliotecas//
int main() {
    int matricula;
    char nome[50];
    float nota1, nota2, media, totalMedia = 0;
    int count = 0;
//declarando variaveis, contador numero de alunos, media da turma iniciando em 0//
/*TABELA CONSULTA------------------------------------
int - %d
char - %s
float - %f ou %2.f (para exibir no max 2 casas decimais)
------------------------------------------------------ */
    printf("Informe as notas do aluno (0 0 para sair):\n");

    while (1) {
        printf("Nota 1: ");
        scanf("%f", &nota1);

        printf("Nota 2: ");
        scanf("%f", &nota2);

        if (nota1 == 0 && nota2 == 0) {
            break;
        }
// lendo notas em loop infinito, armazenando-as interrompendo a leitura quando ambas as notas forem 0//
        printf("Matricula: ");
        scanf("%d", &matricula);

        printf("Nome do Aluno: ");
        scanf("%s", nome);

        media = (nota1 + nota2) / 2;

        totalMedia += media;
        count++;
// lendo matricula, nome e calculando a média//
        printf("Aluno: %s\n", nome);
        printf("Matricula: %d\n", matricula);
        printf("Media: %.2f\n", media);

        if (media >= 7) {
            printf("Situacao: Aprovado\n");
        } else {
            printf("Situacao: Reprovado\n");
        }
// imprime nome, matricula, média e aprovação ou reprovação a partir do calculo da média
        printf("\n");
    }

    if (count > 0) {
        printf("Media da turma: %.2f\n", totalMedia / count);
    } else {
        printf("Nenhum aluno informado.\n");
    }
// quando o usuario informa 0 para ambas as notas (comando para sair), o programa calcula a media da turma se o contador de alunos for maior que 0, caso nao ele informa que não teve registro de alunos.//
    return 0;
}
