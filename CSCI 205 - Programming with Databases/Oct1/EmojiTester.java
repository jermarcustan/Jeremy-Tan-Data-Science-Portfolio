
import javax.swing.*;

public class EmojiTester {

    public static void main(String[] args) {
        int w = 600;
        int h = 600;
        JFrame f = new JFrame();
        Emoji dc = new Emoji(w,h);
        f.setSize(w,h);
        f.setTitle("Drawing in Java");
        f.add(dc);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}