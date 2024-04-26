class gerenciador_de_alunos:

    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome,matricula):
        aluno = {
            "nome": nome,
            "matricula": matricula,
        }
        self.alunos.append(aluno)
        print(f"Nova tarefa foi adicionada: {aluno}")

    def listar_aluno(self):
        print("Lista de alunos:")
        for i, aluno in enumerate(self.alunos, 1):

            print(f"{i}.{aluno['nome']}(matricula:{aluno['matricula']})")

    def remover_aluno(self, indices):
        if 1 <= indices <= len(self.alunos):
            aluno_removido = self.alunos.pop(indices - 1)
            print(f"aluno {aluno_removido} removido com sucesso")
        else:
            print("Índice inválido")

def main(): 
    gerenciador = gerenciador_de_alunos()

    while True:  
        print("---------------------------------------------")
        print("-__--__--__-GERENCIADOR DE ALUNOS-__--__--__-")
        print("---------------------------------------------")
        print("Selecionar opções:")
        print("1:Adicionar alunos")
        print("2:Listar alunos")
        print("3:Remover alunos")
        print("0:sair do programa")
        op =int( input("Digite a opção desejada(0,1,2,3)"))

        if op==1:
                nome = input("Nome do aluno: ")
                matricula=input("digite sua matricula:")
                gerenciador.adicionar_aluno(nome, matricula)
        elif op==2:
                gerenciador.listar_aluno()
        elif op==3:
                indice = int(input("Índice do aluno a ser removido: "))
                gerenciador.remover_aluno(indice)
        else:
                print("Até mais...")
                break
        

if __name__=="__main__":
    main()