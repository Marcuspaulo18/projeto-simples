 package agora_vai;

public class circularchained {
	public static void main (String[] args) {
		Circular_Chained comando = new Circular_Chained();
		for(int i=0;i<=30;i++) {
			comando.insert(i);
		}
		for(int i=0;i<=30;i++) {
			comando.insert_onEnd(i);
		}
		System.out.println("lista após a inserção:");
		comando.show_list();

        System.out.println("Removendo do início: " + comando.remove());
        System.out.println("Lista após remover do início:");
        comando.show_list();

        System.out.println("Removendo do final: " + comando.remove_inEnd());
        System.out.println("Lista após remover do final:");
        comando.show_list();
	}
}
class Nodos{
	public int value;
	public Nodos point;
	public Nodos(int value ) {
		this.value=value;
		this.point=null;
	}
}

 class Circular_Chained{
	Nodos inicio;
	public Circular_Chained() {
		this.inicio=null;
	}
	
	public void insert(int value) {
		Nodos atual = new Nodos(value);
		if(this.inicio==null) {
			atual.point= atual;
			inicio=atual;
		}
		else {
			atual.point= atual;
			inicio=atual;
		}
	}
	public void insert_onEnd(int value) {
		Nodos atual= new Nodos(value);
		if(this.inicio==null) {
			atual.point= atual;
			inicio=atual;
		}
		else {
			Nodos temp=inicio;
			while(temp.point!=inicio) {
				temp=temp.point;
			}
			temp.point= atual;
			atual.point=inicio;
		}
}
	public int remove() {
		if(inicio==null) {
			return -1;
		}
		int value=inicio.value;
		inicio=inicio.point;
		if(inicio==inicio.point) {
			inicio=null;
		}
		return value;
	}
	
	public int remove_inEnd() {
		if(inicio==null) {
			return -1;
		}
		Nodos temp=inicio;
		Nodos prev=null;
		
		while(temp.point!=inicio) {
			prev=temp;
			temp=temp.point;
		}
		
		if(prev==null) {
			inicio=null;
			return temp.value;
		}
		prev.point=inicio;
				return temp.value;
	}
	
	public Boolean isEmpty() {
		return inicio==null;
	}

	public void show_list() {
		if(inicio==null) {
			System.out.println("lista vazia!!!");
			return;
		}
		Nodos temp=inicio;
		do {
			System.out.println(temp.value+"");
			temp=temp.point;
		}while(temp!=inicio);
		System.out.println();
	}
}
