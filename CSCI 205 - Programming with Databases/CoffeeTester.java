public class CoffeeTester {

    public static void main(String[] args) {
        CoffeeMachine kopiko = new CoffeeMachine("KOPIKO");
        CoffeeMachine nescafe = new CoffeeMachine("NESCAFE");
        kopiko.addCoffee(3);
        kopiko.sellCoffee(16);
        nescafe.sellCoffee(13);
        kopiko.sellCoffee(11);
        nescafe.addCoffee(2);
        nescafe.sellCoffee(5);

        kopiko.status();
        nescafe.status();
    }

}