class Biblioteca:
    class Livro:
        def __init__(self):
            self.catalogo = []

        def add_livros(self, titulo, autor, id, status):
            book = {
                "autor": autor,
                "titulo": titulo,
                "id": id,
                "status": status
            }
            self.catalogo.append(book)
            print(f"Novo livro adicionado ao catálogo: {book}")

        def pesquisar_livro(self):
            catal = input("Digite o ID do livro: ")
            for livro in self.catalogo:
                if livro["id"] == catal:
                    print(f"{livro['id']}: {livro['titulo']}: {livro['status']}: {livro['autor']}")
                    return
            print("Livro não encontrado")

    class Membro:
        def __init__(self):
            self.res_member = []

        def add_membros(self, nome, num_membro, emprestimo=None):
            membro = {
                "nome": nome,
                "num_membro": num_membro,
                "emprestimo": emprestimo or []
            }
            self.res_member.append(membro)
            print(f"Membro adicionado: {membro}")

        def emprestimo_livros(self, catalogo, livro_id, membro_num):
            for livro in catalogo:
                if livro["id"] == livro_id:
                    for membro in self.res_member:
                        if membro["num_membro"] == membro_num:
                            print(f"O livro '{livro['titulo']}' foi emprestado ao usuário '{membro['nome']}'")
                            livro["status"] = "emprestado"  # Atualizando o status do livro
                            return
            print("Livro ou membro não encontrado")

    def devol_livro(self, catalogo, livro_id):
        for livro in catalogo:
            if livro["id"] == livro_id:
                if livro["status"] == "emprestado":
                    livro["status"] = "disponível"
                    print("Livro devolvido com sucesso")
                    return
                else:
                    print("Este livro não está emprestado.")
                    return
        print("Livro não encontrado no catálogo")

biblioteca = Biblioteca()
livro_instance = biblioteca.Livro()
membro_instance = biblioteca.Membro()

while True:
    print("-------------------------------------")
    print("------------- BIBLIOTECA -------------")
    print("-------------------------------------")
    print("1: Para adicionar livros")
    print("2: Para adicionar membros")
    print("3: Para permitir empréstimos de livros por membros")
    print("4: Para registrar a devolução de livros")
    print("5: Pesquisar livros por título, autor ou ID")
    print("0: Sair")
    
    op = input("Escolha a opção acima: ")
    
    if op == "0":
        print("Até mais...")
        break
    elif op == "1":
        livro_instance.add_livros(input("Título: "), input("Autor: "), input("ID: "), "disponível")
    elif op == "2":
        membro_instance.add_membros(input("Nome do membro: "), input("Número do membro: "))
    elif op == "3":
        membro_instance.emprestimo_livros(livro_instance.catalogo, input("ID do livro a ser emprestado: "), input("Número do membro que está pegando emprestado: "))
    elif op == "4":
        biblioteca.devol_livro(livro_instance.catalogo, input("ID do livro a ser devolvido: "))
    elif op == "5":
        livro_instance.pesquisar_livro()
