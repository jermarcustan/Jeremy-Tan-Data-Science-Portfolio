import javax.swing.*;
import java.awt.*;

public class CollisionTester {

    public static void main(String[] args) {
        JFrame f = new JFrame();
        CollisionCanvas cc = new CollisionCanvas();
        f.add(cc);
        cc.setPreferredSize(new Dimension(640, 480));
        f.setTitle("Collision Detection");
        f.pack();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);

    }
}