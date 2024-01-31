class gerenciador_de_biblioteca:

    def _init_(self):
     self.livros=[]
     self.emprestimo=[]

    def adicionar_livro(self,autor,titulo,capitulos,genero):
       livro={
        'autor':autor,
        'titulo':titulo,
        'numero de capitulos':capitulos,
        'genero':genero,
        'disponivel':False
        }
       self.livros.append(livro)
       print(f"o livro {livro} foi adicionado a lista")
    
    def listar_livros(self):
     for i,livro in enumerate(self.livros,1):
        adquirida= "adquirida" if livro["disponivel"] else "vago"
        print(f"{i}.{livro['titulo']},{adquirida},autor:{livro['autor']}")
    
    def emprestimo_lista(self):
     for i,livro in enumerate(self.emprestimo,1):
        adquirida= "adquirida" if livro["disponivel"] else "vago"
        print(f"{i}.{livro['titulo']},{adquirida},autor:{livro['autor']}")
    
    def emprestar_livros(self,indice):
      if 1<= indice<= len(self.livros):
        emprestado=self.livros.pop(indice-1)
        emprestado["disponivel"]=True
        print(f"livro {emprestado} garantido com sucesso")
      else:
        print("indice invalido")
    
    def devolver_livros(self,indice):
       if 1<= indice<= len(self.emprestimo):
        devolvido=self.livros.pop(indice-1)
        devolvido["disponivel"]=False
        self.livros.append(devolvido)
        print(f"livro {devolvido} devolvido com sucesso")
       else:
        print("indice invalido")
    
    
