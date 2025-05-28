import java.awt.*;

public class MyRectangle {
    private int x;
    private int y;
    private int width;
    private int height;


    public MyRectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    public void draw(Graphics g) {
        g.fillRect(x, y, width, height);
    }

    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public boolean isColliding(MyRectangle other) {
        return !(this.x + this.width <= other.getX() ||
        this.x >= other.getX() + other.getWidth() ||
        this.y + this.height <= other.getY() ||
        this.y >= other.getY() + other.getHeight() );
    }
    


}