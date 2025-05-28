public class Attraction {

    private String name;
    public double cost;

    public Attraction(String n, double c) {
        name = n;
        cost = c;
    }

    public String getName() {
        return name;
    }
    
    public double getCost() {
        return cost;
    }
}
