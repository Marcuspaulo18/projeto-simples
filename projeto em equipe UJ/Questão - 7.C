    #include <stdio.h>
    #include <stdbool.h>
    #include <math.h>
//bibliotecas//
    int main() {
    double a, b, c, D, x1, x2, sx, cnnr;
//declarando variaveis//
    while (a!=0)
    {
//loop enquanto a for diferente de 0//
    
    printf("Infome valor de A, B e C(informe 0 em todos para encerrar)\n");
    scanf("%lf %lf %lf", &a, &b, &c);
    
//solicita e registra os valores de a,b e c//
if (a==0 && b==0 && c==0 )

{
    break;
}

    D=(b*b-4*a*c);
//calcula delta//    
    if (D<0)
    {
        cnnr = cnnr+2;
        printf("Raizes complexas\n");
    } 
    else{
// contador de raizes complexas//
    x1=((-b-sqrt(D)) / (2*a));
    x2=((-b+sqrt(D)) / (2*a));
    printf("As raizes sao %lf", x1);
    printf("e %lf \n", x2);
//calcula as raizes e e exibe na tela//
    if (x1==x2)
    {
        sx=x1+x2;
        printf("A soma das raizes eh: %lf", sx);
    }
//se as raizes forem iguais, soma-as e exibe na tela//
    }
    }
    printf("O numero de raizes complexas lidas eh %lf", cnnr);
        return 0;
//exibe na tela o total de raizes
    }
