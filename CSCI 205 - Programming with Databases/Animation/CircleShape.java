import java.awt.*;
import java.awt.geom.*;

public class CircleShape {
    private double x;
    private double y;
    private double size;
    private Color color;
    
    public CircleShape(double x, double y, double size, Color color) {
        this.x = x;
        this.y = y;
        this.size = size;
        this.color = color;
    }

    public void draw(Graphics2D g2d) {
        Ellipse2D.Double c = new Ellipse2D.Double(x,y,size, size);
        g2d.setColor(color);
        g2d.fill(c);

    }

    public void moveH(double n) {
        x += n;
    }
}
