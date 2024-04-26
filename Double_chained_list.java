package agora_vai;

public class Double_chained_list {
	public static void main(String[] args) {
		Lista_D_Encadeada lista= new Lista_D_Encadeada();
		for(int i=0;i<=10;i++) {
			lista.inserir(i);
		}
		for(int r=0;r<=5;r++) {
			lista.remover(r);
		}
		System.out.println(lista.contarlist());
	}
	}

 class Nostro{
	 public int valor;
	 public Nostro proxi;
	 public Nostro anterio;
	 public Nostro(int valor) {
		 this.valor=valor;
		 this.proxi=null;
		 this.anterio=null;
	 }
 }
class Lista_D_Encadeada{
	Nostro inicio;
	public Lista_D_Encadeada(){
		this.inicio = null;
	}

public void inserir(int valor){
	if(this.inicio==null) {
		this.inicio= new Nostro(valor);
	}
	else {
		Nostro atual=this.inicio;
		while(atual.proxi!= null) {
			atual.proxi=atual;
		}
		Nostro novoNo= new Nostro(valor);
		atual.proxi=novoNo;
		novoNo.anterio=atual;
	}
}

public void remover(int valor) {
	if(this.inicio==null){ 
		System.out.println("lista vazia");
		
	}
	else {
		Nostro atual=this.inicio;
		while(atual!=null && atual.valor!=valor) {
			atual=atual.proxi;
		}
		if(atual.anterio!=null&& atual!=null) {
			atual.anterio.proxi=atual.anterio;
		}
		else {
			this.inicio=atual.proxi;
		}
		if(atual.proxi!=null) {
			atual.anterio.proxi=atual.proxi;
		}
	}
}

public int contarlist() {
	int count=0;
	Nostro atual= this.inicio;
	while(atual!=null) {
		count++;
		atual=atual.proxi;
	}
	return count;

}
}
