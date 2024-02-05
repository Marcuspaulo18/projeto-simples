import biblioteca
""" codigo não terminado 100% """
print("--------------BIBLIOTECON---------------")
print("a sua biblioteca digital")
print("digite 0 para sair do programa")
print("digite 1 para adicionar um livro")
print("digite 2 para listar todos os livros")
print("digite 3 para fazer um emprestimo de livro")
print("digite 4 para devolver um livro")
print("digite 5 para ler os livros emprestados")

while(True):
    print("digite 0 para sair do programa")
    print("digite 1 para adicionar um livro")
    print("digite 2 para listar todos os livros")
    print("digite 3 para fazer um emprestimo de livro")
    print("digite 4 para devolver um livro")
    print("digite 5 para ler os livros emprestados")
    variavel=int(input("digite uma opção entre 0,1,2,3,4,5:"))
    match variavel:
        case 0:
            print("Boa leitura...")
            break
        case 1:
            autor=str(input(""))
            titulo=str(input(""))
            capitulos=str(input(""))
            genero=str(input(""))
            biblioteca.gerenciador_de_biblioteca.adicionar_livro(autor,titulo,capitulos,genero)
        case 2:
            indice=int(input("digite o indice do livro que deseja pegar"))
            biblioteca.gerenciador_de_biblioteca.listar_livros(indice)
        case 3:
            indice=int(input("digite o indice do livro que deseja pegar"))
            biblioteca.gerenciador_de_biblioteca.emprestar_livros(indice)
        case 4:
            biblioteca.gerenciador_de_biblioteca.emprestimo_lista()
        case 5:
            indice=int(input("digite o indice do livro que deseja pegar"))
            biblioteca.gerenciador_de_biblioteca.devolver_livros(indice)
