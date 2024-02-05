print("--------------ANALISADOR DE STRING 5000--------------")
import manipulacao_strings
string=str(input("digite uma string:"))

while(True):
    print("digite 1 para inverter a string")
    print("digite 2 para saber o numero de palavras da string")
    print("digite 3 para verificar se uma string é um palindromo")
    print("digite 0 para sair do programa")
    variavel=int(input("digite entre 0,1,2 ou 3 "))
    match variavel:
       case 1:
            print(manipulacao_strings.inverter(string))
       case 2:
            print(manipulacao_strings.contar(string))
       case 3:
            print(manipulacao_strings.palindromo(string))
       case 0:
            break