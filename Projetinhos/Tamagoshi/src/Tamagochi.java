public class Tamagochi {

	private String name;
	private int age;
	private double health;
	private double hapiness;
	private double hunger;
	
	public Tamagochi(String name, int age, double health, double hapiness, double hunger) {
		this.name = name;
		this.age = age;
		this.health = health;
		this.hapiness = hapiness;
		this.hunger = hunger;
	}
	
	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public double getHealth() {
		return health;
	}
	public void setHealth(int health) {
		this.health = health;
	}
	public double getHapiness() {
		return hapiness;
	}
	public void setHapiness(int hapiness) {
		this.hapiness = hapiness;
	}
	public double getHunger() {
		return hunger;
	}
	public void setHunger(int hunger) {
		this.hunger = hunger;
	}
	
	public void hungry() {
        hunger -= 15;
        if(hunger <= 50) {
    		System.out.println(name +" est� ficando com fome, alimente-o(a)!");
        }else if (hunger >= 100) {
        	hunger = 100;
        	System.out.println(name +" est� satisfeito!");
        }else if(hunger <= 0) {
        	hunger = 0;
        	System.out.println(name +" est� com fome, alimente-o(a)!");
        }
    }
	public void sadness() {
        hapiness -= 15;
        if(hapiness <= 50) {
        	System.out.println(name +" est� ficando triste, deixe-o(a) feliz!");
        }else if (hapiness >= 100) {
        	hapiness = 100;
        	System.out.println(name +" est� feliz!");
        }else if (hapiness <= 0) {
        	hapiness = 0;
        	System.out.println(name +" est� triste, deixe-o(a) feliz!");
        }
    }
	public void dying() {
        health -= 10;
        if (health <= 0) {
        	health = 0;
        	System.out.println(name+" est� morto...");
        }
    }
	public void older() {
		age += 1;
		if (age >= 10) {
			System.out.println(name +" est� ficando velhinho(a)");
		}else if (age >= 11) {
			health -= 25;
		}
	}
	public void play() {
		hapiness += 35;
		if (hapiness <= 100) {
			System.out.println("Voc� brincou com "+ name +", ele parece estar mais feliz!");
		}
    }
	public void eat() {
		hunger += 35;
		health += 10;
		if (hunger <= 100) {
	        System.out.println(name +" foi alimentado");
		}
    }
	
	public void statusIncrease() {
		System.out.println();
		hungry();
		sadness();
		dying();
		older();
		System.out.println();
	}
	public void print() {
		System.out.println("Nome: "+ name);
		System.out.println("Idade: "+ age);
		System.out.println("Sa�de: "+ health);
		System.out.println("Fome: "+ hunger);
		System.out.println("Felicidade: "+ hapiness);
	}
}