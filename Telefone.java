package agora_vai;

public class Telefone {
public static void main(String[]args) {
	Agenda comando =new Agenda();
    comando.inserir("João", "11 9999-9999");
    comando.inserir("Maria", "12 8888-8888");
    comando.inserir("Pedro", "13 7777-7777");
    comando.inserir("marcus", "71 99401-0727");
    System.out.println("Telefone da Maria: " + comando.buscar("Maria"));

    comando.remover("João");

    comando.imprimir();
}
}
class Contato{
	String nome;
	String telefone;
	Contato proximo;
	public Contato(String nome,String telefone) {
		this.nome=nome;
		this.telefone=telefone;
		this.proximo=null;
	}


public String getNome() {
    return nome;
}

public void setNome(String nome) {
    this.nome = nome;
}

public String getTelefone() {
    return telefone;
}

public void setTelefone(String telefone) {
    this.telefone = telefone;
}

public Contato getProximo() {
    return proximo;
}

public void setProximo(Contato proximo) {
    this.proximo = proximo;
}
}
class Agenda{
	Contato primeiro;
	Contato ultimo;
	public Agenda() {
		this.primeiro=null;
		this.ultimo=null;
	}
	
	public void inserir(String nome,String telefone) {
		Contato novoContato= new Contato(nome,telefone);
		if(primeiro==null) {
			primeiro=ultimo=novoContato;
		}
		else {
			ultimo.setProximo(novoContato);
			ultimo=novoContato;
		}
	}
	public void remover(String nome) {
		Contato contatoAnterior=null;
		Contato contatoAtual=primeiro;
		while(contatoAtual!=null) {
			if(contatoAtual.getNome()==nome) {
				if(contatoAnterior==null) {
					primeiro=contatoAtual.getProximo();
				}
				else {
					contatoAnterior.setProximo(contatoAtual.getProximo());
				}
				if(contatoAtual==ultimo) {
					ultimo= contatoAnterior;
				}
				break;
			}
			contatoAnterior=contatoAtual;
			contatoAtual=contatoAtual.getProximo();
		}
	}
	public String buscar(String nome) {
		Contato contatoAtual=primeiro;
		while(contatoAtual!=null) {
			if(contatoAtual.getNome()==nome) {
				return contatoAtual.getTelefone();
			}
			contatoAtual=contatoAtual.getProximo();
		}
		return null;
	}
	public void imprimir() {
		Contato contatoAtual=primeiro;
		while(contatoAtual!=null) {
			System.out.println("Nome:"+contatoAtual.getNome());
			System.out.println("telefone:"+contatoAtual.getTelefone());
			
			contatoAtual=contatoAtual.getProximo();
		}
	}
}