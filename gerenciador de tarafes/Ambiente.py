class gerenciador_de_tarefas:

    def __list__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, categoria, descricao):
        tarefa = {
            "nome": nome,
            "categoria": categoria,
            "descricao": descricao,
            "concluida": False,
        }
        self.tarefas.append(tarefa)
        print(f"Nova tarefa foi adicionada: {tarefa}")

    def listar_tarefas(self):
        print("Lista de tarefas:")
        for i, tarefa in enumerate(self.tarefas, 1):
            concluida = "concluída" if tarefa["concluida"] else "pendente"
            print(f"{i}.{tarefa['nome']}({concluida},Categoria:{tarefa['categoria']})")

    def marcar_como_concluida(self, indice):
        if 1 <= indice <= len(self.tarefas):
            self.tarefas[indice - 1]["concluida"] = True
            print(f"Tarefa {indice} foi concluída")
        else:
            print("Índice inválido")

    def exibir_por_categoria(self,indice,categoria):
           if 1 <= indice <= len(self.tarefas):
            self.tarefas[indice - 1]["categoria"] = categoria
            print(f"Tarefa {indice} foi categorizada como {categoria}")
           else:
            print("Índice inválido")

    def remover_tarefa(self, indices):
        if 1 <= indices <= len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indices - 1)
            print(f"Tarefa {tarefa_removida} removida com sucesso")
        else:
            print("Índice inválido")

def main(): 
    gerenciador = gerenciador_de_tarefas()

    while True:  
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("-__--__--__GERENCIADOR DE TAREFAS__--__--__-")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("Selecionar opções:")
        print("1:Adicionar tarefas")
        print("2:Listar tarefas")
        print("3:Remover tarefas")
        print("4:Exibir por categoria")
        print("5:Marcar como concluida")
        print("6:Sair do programa")
        op = input("Digite a opção desejada(1,2,3,4,5,6)")

        match op:
            case "1":
                nome = input("Nome da tarefa: ")
                descricao = input("Descrição da tarefa: ")
                categoria = input("Categoria da tarefa: ")
                gerenciador.adicionar_tarefa(nome, descricao, categoria,)
            case "2":
                gerenciador.listar_tarefas()
            case "3":
                indice = int(input("Índice da tarefa a ser removida: "))
                gerenciador.remover_tarefa(indice)
            case "4":
                indice = int(input("Índice da tarefa a ser categorizada: "))
                categoria = input("Nova categoria: ")
                gerenciador.exibir_por_categoria(indice, categoria)
            case "5":
                indice = int(input("Índice da tarefa a ser concluída: "))
                gerenciador.marcar_como_concluida(indice)
            case "6":
                print("Até mais...")
                break


if __name__=="__main__":
    main()

