package agora_vai;

public class Chained_list {
public static void main(String[] args1) {
	ListaEncadeada lista=new ListaEncadeada();
	for(int i=1;i<100;i++) {
		lista.inserir(i);
	}
	for(int m=1;m<=50;m++) {
		lista.remover(m);
	}
	System.out.println(lista.ContarValor());
}
}

class No{
	public int valor;
	public No point;
	public No(int valor) {
		this.valor=valor;
		this.point=null;
	}
}

class ListaEncadeada{
	No inicio;
	public ListaEncadeada() {
		this.inicio=null;
	}
	public void inserir(int valor) {
		if(this.inicio==null) {
			this.inicio= new No(valor);
		}
		else {
			No atual=this.inicio;
			while(atual.point!=null) {
				atual=atual.point;
			}
			atual.point=new No(valor);
		}
	}
	public void remover(int valor) {
		if(this.inicio==null) {
			System.out.println("não há nenhum item na lista");
		}
		else {
			No anterior=this.inicio;
			No atual=this.inicio;
			while(atual.valor!=valor) {
				anterior=atual;
				atual=atual.point;
			}
			anterior.point=atual.point;
		}
	}
	public int ContarValor() {
		int cont=0;
		if(this.inicio!=null) {
			cont=1;
			No atual=this.inicio;
			while(atual.point!=null) {
				cont++;
				atual=atual.point;
			}
		}
		return cont;
	}
	
}
