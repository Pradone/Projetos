import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String action;
        String witch;
        
        System.out.println("Adicione o nome do primeiro tamagochi ");
        String name1 = input.next();
        System.out.println("Adicione o nome do segundo tamagochi ");
        String name2 = input.next();
        
        Tamagochi tama1 = new Tamagochi (name1, 1, 100, 100, 100);
        Tamagochi tama2 = new Tamagochi (name2, 1, 100, 100, 100);
        System.out.println();
        
        do {
        	tama1.print();
	        System.out.println();
	        tama2.print();
	        System.out.println();
	        System.out.println("O que gostaria de fazer?");
	        action = input.next();
	        
	        
	        if (action.equals("sair")) {
	        	break;
	        }else if (action.equals("alimentar")){
	        	System.out.println("Qual?");
	        	witch = input.next();
	        	if(witch.equals("1") | witch.equals(name1)) {
	        		tama1.eat();
	        	}else if (witch.equals("2") | witch.equals(name2)) {
	        		tama2.eat();
	        	}else if (witch.equals("ambos")) { 
	        		tama1.eat();
	        		tama2.eat();
	        	}
	        }else if(action.equals("brincar")) {
	        	System.out.println("Qual?");
	        	witch = input.next();
	        	if(witch.equals("1") | witch.equals(name1)) {
	        		tama1.play();
	        	}else if (witch.equals("2") | witch.equals(name2)) {
	        		tama2.play();
	        	}else if (witch.equals("ambos")) { 
	        		tama1.play();
	        		tama2.play();
	        	}
	        }
	        tama1.statusIncrease();
        	tama2.statusIncrease();
        }while (true);
        input.close();
        
        System.out.println("Encerrando Programa...");
        try {
        	Thread.sleep(1750);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Programa encerrado");
	}

}
