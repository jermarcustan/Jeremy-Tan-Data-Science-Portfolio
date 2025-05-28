import java.awt.*;

public class MyCircle {

    private int x;
    private int y;
    private int radius;

    public MyCircle(int x, int y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public void draw(Graphics g) {
        g.fillOval(x, y, radius*2, radius*2);
    }

    public double getX() {
        return x;
    }
    
    public double getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public double square(double x) {
        return x*x;
    }

    public boolean isColliding(MyCircle other) {
        return ( Math.sqrt(square(this.x + this.radius - other.x - other.radius) + square( this.y + this.radius - other.x - other.radius)) < (this.radius + other.radius) );
    }   
}