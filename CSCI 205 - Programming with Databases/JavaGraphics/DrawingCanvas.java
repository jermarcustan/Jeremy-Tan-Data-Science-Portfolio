package JavaGraphics;

import java.awt.*;
import java.awt.geom.*;
import javax.swing.*;

public class DrawingCanvas extends JComponent {

    private int width;
    private int height;
    private Cloud c1;
    private Cloud c2;
    private Cloud c3;

    public DrawingCanvas(int w, int h) {

        width = w;
        height = h;
        c1 = new Cloud(10,50,75,Color.LIGHT_GRAY);
        c2 = new Cloud(200,75,90,Color.BLUE);
        c3 = new Cloud(420,60,85,Color.DARK_GRAY);
    }
    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        RenderingHints rh = new RenderingHints(
            RenderingHints.KEY_ANTIALIASING,
            RenderingHints.VALUE_ANTIALIAS_ON);
        
        g2d.setRenderingHints(rh);
        
        Rectangle2D.Double r1 = new Rectangle2D.Double(250,200,100,100);
        Rectangle2D.Double r2 = new Rectangle2D.Double(100,150,100,100);
        Rectangle2D.Double r3 = new Rectangle2D.Double(50,50,100,100);

        AffineTransform reset = g2d.getTransform();

        g2d.rotate(Math.toRadians(15), 250, 200);
        g2d.setColor(Color.RED);
        g2d.fill(r1);
        g2d.setTransform(reset);
        g2d.rotate(Math.toRadians(30), 250, 200);
        g2d.setColor(Color.BLUE);
        g2d.fill(r1);
        
        g2d.setTransform(reset);
        c1.drawCloud(g2d);
        c2.drawCloud(g2d);
        c3.drawCloud(g2d);


        
    }

}
