def inverter(string):
    return string[::-1]

def palindromo(string):
    if(string == string[::-1]):
        print(f"a string {string} é um palindromo, por curiosidade, ela invertida é {string[::-1]}")
    else:
        print("não é uma string")

def contar(string):
    contado=len(string)
    print(f"o numero de palavras dentro da string é {contado}")