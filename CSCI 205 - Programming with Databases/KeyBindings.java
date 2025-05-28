import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class KeyBindings {
    private JFrame f;
    private JPanel cp;

    public KeyBindings() {
        f = new JFrame();
        cp = (JPanel) f.getContentPane();
        cp.setFocusable(true);

    }

    public void setUpGUI() {
        f.setSize(320, 240);
        f.setTitle("Key Bindings");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);

    }

    public void addKeyBindings() {
        ActionMap am = cp.getActionMap();
        InputMap im = cp.getInputMap();

        AbstractAction doSomething = new AbstractAction() {

            @Override
            public void actionPerformed(ActionEvent ae) {
                System.out.println("do something");
            }
        };

        AbstractAction doMoreThings = new AbstractAction() {

            @Override
            public void actionPerformed(ActionEvent ae) {
                System.out.println("more things!");
            }
        };

        am.put("ds", doSomething);
        am.put("dmt", doMoreThings);

        im.put(KeyStroke.getKeyStroke(KeyEvent.VK_UP, 0, false), "ds");
        im.put(KeyStroke.getKeyStroke(KeyEvent.VK_DOWN, 0, false), "dmt");
    }

 
}



