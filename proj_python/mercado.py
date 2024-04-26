class gerenciador_de_produtos:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto, valor, quantidade):
        total = valor * quantidade  
        totalProduto = { 
            "produto": produto,
            "valor": valor,
            "total": total,
            "quantidade": quantidade,
        }
        self.produtos.append(totalProduto)
        print(f"Novo produto foi adicionado: {totalProduto}")
        if valor and total<0:
            print("digite um valor positivo")
    def listar_produto(self):
        print("Lista de produtos:")
        for i, totalProduto in enumerate(self.produtos, 1):
            print(f"{i}.{totalProduto['produto']}/{totalProduto['valor']}/R${totalProduto['total']}/quantidade{totalProduto['quantidade']}")

    def atualizar_produto(self, produto, novo_produto, novo_valor, novo_quantidade): 
        produto_atualizado = False
        novo_total=novo_quantidade*novo_valor
        for totalProduto in self.produtos:
            if totalProduto['produto'] == produto:
                totalProduto['produto'] = novo_produto
                totalProduto['valor'] = novo_valor
                totalProduto['quantidade'] = novo_quantidade
                totalProduto['total']=novo_total
                produto_atualizado = True
                break
        if produto_atualizado:
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
        if novo_total and novo_valor<0:
            print("por favor digite um valor positivo")
    def remover_produto(self, produto):
        produto_removido = None
        for totalProduto in self.produtos:
            if totalProduto['produto'] == produto:
                produto_removido = totalProduto  
                break
        if produto_removido:
            self.produtos.remove(produto_removido)
            print(f"Produto {produto_removido['produto']} removido com sucesso")  
        else:
            print("Produto não encontrado.")

def main(): 
    gerenciador = gerenciador_de_produtos()

    while True:  
        print("-----------------------------------------------")
        print("-__--__--__ GERENCIADOR DE PRODUTOS __--__--__-")
        print("-----------------------------------------------")
        print("Selecionar opções:")
        print("1: Adicionar produto")
        print("2: Listar produtos")
        print("3: Remover produto")
        print("4: Atualizar produto")
        print("5: Sair do programa")
        op = input("Digite a opção desejada(1,2,3,4,5): ")

        if op == "1":  
            produto = input("Nome do produto: ")
            valor = float(input("Valor do produto: "))  
            quantidade = int(input("Quantidade do produto: "))  
            gerenciador.adicionar_produto(produto, valor, quantidade)
        elif op == "2":
            gerenciador.listar_produto()
        elif op == "3":
            produto = input("Produto a ser removido: ")
            gerenciador.remover_produto(produto)
        elif op == "4":
            produto = input("Produto a ser atualizado: ")
            novo_produto = input("Novo nome do produto: ")
            novo_valor = float(input("Novo valor do produto: "))  
            novo_quantidade = int(input("Nova quantidade do produto: "))  
            gerenciador.atualizar_produto(produto, novo_produto, novo_valor, novo_quantidade)
        elif op == "5":
            print("Até mais...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
