import javax.swing.*;
import java.awt.*;

public class CollisionCanvas extends JComponent {

    private MyCircle c1;
    private MyCircle c2;

    public CollisionCanvas() {
        c1 = new MyCircle(0,0,50);
        c2 = new MyCircle(125,50,50);
    }
    protected void paintComponent(Graphics g) {
        g.setColor(Color.GREEN);
        c1.draw(g);
        g.setColor(Color.RED);
        c2.draw(g);

        System.out.println(c1.isColliding(c2));
        
    }
}