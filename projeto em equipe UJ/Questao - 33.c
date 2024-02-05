#include <stdio.h>

int main() {
    // Declaração de variáveis
    int dia, mes, ano, x, y, z;
    int datas[64][3];  // Array para armazenar as datas
    int cont = 0;      // Contador para o número de datas inseridas

    // Loop externo para até 64 iterações
    for (x = 0; x < 64; x++) {
        // Loop do meio
        for (y = 0; y < 64; y++) {
            // Loop interno
            for (z = 0; z < 64; z++) {
                // Solicita ao usuário inserir uma data
                printf("Digite uma data no formato DD/MM/AAAA.\n");
                scanf("%d/%d/%d", &dia, &mes, &ano);

                // Verifica se o usuário digitou 0/0/0 para encerrar a entrada de datas
                if (dia == 0 && mes == 0 && ano == 0) {
                    break;
                }

                // Armazena a data no array e incrementa o contador
                datas[cont][0] = dia;
                datas[cont][1] = mes;
                datas[cont][2] = ano;
                cont++;
            }

            // Verifica se o usuário digitou 0/0/0 para encerrar a entrada de datas
            if (dia == 0 && mes == 0 && ano == 0) {
                break;
            }
        }

        // Verifica se o usuário digitou 0/0/0 para encerrar a entrada de datas
        if (dia == 0 && mes == 0 && ano == 0) {
            break;
        }
    }

    // Loop para ordenar as datas em ordem cronológica
    for (int i = 0; i < cont; i++) {
        for (int j = i + 1; j < cont; j++) {
            // Compara as datas e troca se estiverem fora de ordem
            if (datas[i][2] > datas[j][2] || (datas[i][2] == datas[j][2] && datas[i][1] > datas[j][1]) ||
                (datas[i][2] == datas[j][2] && datas[i][1] == datas[j][1] && datas[i][0] > datas[j][0])) {
                // Troca as datas usando uma variável temporária
                int temp[3];
                for (int k = 0; k < 3; k++) {
                    temp[k] = datas[i][k];
                    datas[i][k] = datas[j][k];
                    datas[j][k] = temp[k];
                }
            }
        }
    }

    // Loop para imprimir as datas em ordem cronológica
    for (int i = 0; i < cont; i++) {
        printf("%02d/%02d/%04d\n", datas[i][0], datas[i][1], datas[i][2]);
    }

    return 0;
}

    