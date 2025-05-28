
import java.awt.*;
import java.awt.geom.*;
import javax.swing.*;

public class Emoji extends JComponent {

    private int width;
    private int height;

    public Emoji(int w, int h) {
        width = w;
        height = h;
    }

    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        
        RenderingHints rh = new RenderingHints(
            RenderingHints.KEY_ANTIALIASING,
            RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.setRenderingHints(rh);
        g2d.setColor(new Color(255, 203, 76));
        Ellipse2D.Double face = new Ellipse2D.Double(100,100,400,400);
        g2d.fill(face);

        g2d.setColor(Color.BLACK);
        Ellipse2D.Double left_eye = new Ellipse2D.Double(200, 200, 50, 50);
        Ellipse2D.Double right_eye = new Ellipse2D.Double(350, 200, 50, 50);
        g2d.fill(left_eye);
        g2d.fill(right_eye);

        Arc2D.Double mouth = new Arc2D.Double(200, 250, 200, 150, 0, -180, Arc2D.OPEN);
        g2d.fill(mouth);
        
        g2d.setColor(new Color(249, 108, 186));

        Rectangle2D.Double uppertongue = new Rectangle2D.Double(247.5, 350, 105, 100); 
        Ellipse2D.Double lowertongue = new Ellipse2D.Double(245, 350, 110, 150);
        g2d.fill(uppertongue);
        g2d.fill(lowertongue);
    }
}