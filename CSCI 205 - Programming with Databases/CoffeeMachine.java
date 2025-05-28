public class CoffeeMachine {
    
    private double coffee_amt;
    private double sales;
    private int cups;
    private double price;
    private String company_name;

    public CoffeeMachine(String company_name) {
        cups = 0;
        sales = 0;
        coffee_amt = 5;
        price = 45.54;
        this.company_name = company_name;

    }

    public void addCoffee(double refill) {

        coffee_amt += refill;

    }

    public void sellCoffee(int numCups) {

        cups += numCups;
        sales += price*numCups;
        coffee_amt = coffee_amt - numCups*0.25;

    }

    public double getCoffeeLeft() {

        return coffee_amt;
    }

    public int getCupsSold() {

        return cups;

    }

    public double getSales() {

        return sales;

    }

    public String getName() {
        return company_name;
    }

    public void status() {

        System.out.println("----- " + getName() + " MACHINE -----");
        System.out.println("Cups of Coffee Sold: " + getCupsSold());
        System.out.printf("Remaining Coffee: %f liters\n", getCoffeeLeft());
        System.out.println("Total Sales: PHP " + getSales());

    }

}
