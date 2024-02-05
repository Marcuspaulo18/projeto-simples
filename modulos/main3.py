import random
print("--------------ADIVINHATRON--------------")
print("o seu joguinho pra passar o tempo")
nome=input("digite o seu nome:")
print(f"Bem vindo {nome}")
print("vamos começar...")
min=int(input("digite o valor maximo"))
max=int(input("digite o valor minimo"))
tentativa=0
randomico=random.randint(min,max)
while(True):
 numero=int(input("digite o numero:"))
 if( numero == None):
      print("digite um numero")
 elif(numero<min or numero>max):
      print("por favor digite um numero dentro da margem desejada")  
 else:
     tentativa+=1
     if(numero>randomico):
         print(f"{numero},muito alto! chuta mais baixo")
     elif(numero<randomico):
          print(f"{numero},muito baixo! chuta mais alto")
     else:
         print("YOU WIN!")
         print(f"parabens {nome} você conseguiu achar o numero {numero} apos {tentativa} tentativas")
     