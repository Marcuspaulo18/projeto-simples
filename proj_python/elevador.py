class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar 
        self.atualAndar = 1

    def reformular(self, novacap, novoand):
        self.totalAndar = novoand
        self.totalCapacidade = novacap
        print(f"capacidade atual: {self.totalCapacidade}/andares totais: {self.totalAndar}")

    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("subindo...")
        else:
            print("Lamento mas não consigo subir mais")

    def descer(self):
        if self.atualAndar > 1:
            self.atualAndar -= 1
            print("descendo...")
        else:
            print("lamento mas não consigo descer mais")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando...")
        else:
            print("lamento mas a capacidade máxima foi atingida, aguarde...")

    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("saindo...")
        else:
            print("lamento mas não tem ninguém.")

elevador = Elevador(0, 0)

while True:
    print("<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<ELEVATOR.I.A>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>")
    print("1: formular o número de andares e capacidade de pessoas dentro do elevador")
    print("2: subir um andar")
    print("3: descer um andar")
    print("4: permitir a entrada de pessoas no elevador")
    print("5: diminuir a quantidade de pessoas do elevador")
    print("6: desligar o elevador")
    
    var = input("selecione uma alternativa:")
    
    match(var):
        case "1":
            novacap = int(input("digite a quantidade de pessoas: "))
            novoand = int(input("digite a quantidade de andares: "))
            elevador.reformular(novacap, novoand)
        
        case "2":
            elevador.subir()
        
        case "3":
            elevador.descer()
        
        case "4":
            elevador.entrar()
        
        case "5":
            elevador.sair()
        
        case "6":
            print("Desligando...")
            break