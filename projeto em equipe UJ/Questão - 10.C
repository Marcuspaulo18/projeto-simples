#include <stdio.h>
#include <math.h>
//bibliotecas//
int main() {
    const float valorHora = 35.0;
    const float taxaINSS = 8.5;
    const float taxaSindicato = 1.02;
    const float taxaPlanoSaude = 6.0;
//declaração de constantes das taxas de contribuição, e valor da hora de trabalho//
    int matricula;
    char nome[100];
    float horasTrabalhadas;
    float salarioBruto, salarioLiquido;
    float totalFolhaPagamento = 0;
    float totalContribuicaoINSS = 0;
    float totalContribuicaoSindicato = 0;
    float totalContribuicaoPlanoSaude = 0;
//declaração das variaveis para armazenar matricula,nome,horas,salario bruto e liquido e os totais para relatorio//
/*TABELA CONSULTA------------------------------------
int - %d
char - %s
float - %f ou %2.f (para exibir no max 2 casas decimais)
------------------------------------------------------ */
    while (1) {
        printf("Informe a matricula (ou 0000 para sair): ");
        scanf("%d", &matricula);

        if (matricula == 0) {
            break;
        }
// inicia o loop infinito solicitando a matricula, finalizando quando a matricula for nula//
        printf("Informe o nome do funcionario: ");
        scanf("%s", nome);

        printf("Informe o total de horas trabalhadas: ");
        scanf("%f", &horasTrabalhadas);
// solicita e armazena o nome e o total de horas trabalhadas//
        salarioBruto = horasTrabalhadas * valorHora;
        totalFolhaPagamento += salarioBruto;
// calcula o salario bruto e atualiza o total da folha de pagamento//
        float contribuicaoINSS = (salarioBruto * taxaINSS) / 100.0;
        totalContribuicaoINSS += contribuicaoINSS;

        float contribuicaoSindicato = (salarioBruto * taxaSindicato) / 100.0;
        totalContribuicaoSindicato += contribuicaoSindicato;

        float contribuicaoPlanoSaude = (salarioBruto * taxaPlanoSaude) / 100.0;
        totalContribuicaoPlanoSaude += contribuicaoPlanoSaude;
// calcula individualmente as contribuições em cima do salario bruto//
        salarioLiquido = salarioBruto - contribuicaoINSS - contribuicaoSindicato - contribuicaoPlanoSaude;
// calcula o salarioliquido subtraindo as contribuições do salario bruto//
        printf("\nResumo do funcionario:\n");
        printf("Matricula: %d\n", matricula);
        printf("Nome: %s\n", nome);
        printf("Salario Bruto: R$%.2f\n", salarioBruto);
        printf("Salario Liquido: R$%.2f\n", salarioLiquido);
// imprime o relatorio individual do funcionario//
        printf("\n");
    }

    printf("\nResumo Geral:\n");
    printf("Total da Folha de Pagamento: R$%.2f\n", totalFolhaPagamento);
    printf("Total de Contribuicao para o INSS: R$%.2f\n", totalContribuicaoINSS);
    printf("Total de Contribuicao para o Sindicato: R$%.2f\n", totalContribuicaoSindicato);
    printf("Total de Contribuicao para o Plano de Saude: R$%.2f\n", totalContribuicaoPlanoSaude);
// quando o loop é finalizado, imprime o resumo geral com o total da folha de pagamento e o total de cada tipo de contribuição //
    return 0;
}
