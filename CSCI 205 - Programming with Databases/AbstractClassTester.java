import java.util.ArrayList;

public class AbstractClassTester {

    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>();
        shapes.add(new Circle("blue"));
        shapes.add(new Square("red"));

        for(Shape s: shapes) {
            s.describe();
        }
    }
}