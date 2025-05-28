public abstract class Shape {

    public String color;

    public Shape() {

        System.out.println("A shape has been instantiated.");
    }

    public Shape(String c) {
        color = c;
    }
    public abstract void draw();

    public void describe() {
        System.out.println("This is a shape.");
        System.out.println("It's color is " + color);
    }

    public String getColor() {
        return color;
    }
}