import javax.swing.*;
import java.awt.*;
import java.awt.geom.*;

public class AnimationCanvas extends JComponent{
    private int width;
    private int height;
    private Color bgColor;
    private CircleShape circle;
    

    public AnimationCanvas(int w, int h, Color bgc) {
        width = w;
        height = h;
        bgColor = bgc;
        circle = new CircleShape(20, 40, 100, Color.BLUE);
        setPreferredSize(new Dimension(width, height));
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        RenderingHints rh = new RenderingHints(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.setRenderingHints(rh);

        Rectangle2D.Double background = new Rectangle2D.Double(0,0,width,height);
        g2d.setColor(bgColor);
        g2d.fill(background);

        circle.draw(g2d);

    }

    public CircleShape getCircle() {
        return circle;
    }





}