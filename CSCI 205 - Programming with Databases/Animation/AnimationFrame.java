import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class AnimationFrame {
    private JFrame frame;
    private JButton button;
    private AnimationCanvas animationCanvas;

    public AnimationFrame() {
        frame = new JFrame();
        button = new JButton("CLICK ME");
        animationCanvas = new AnimationCanvas(640, 480, Color.CYAN);

    }

    public void setUpButtonListener() {
        ButtonListener bl = new ButtonListener();
        button.addActionListener(bl);
    }

    public void setUpGUI() {
        Container cp = frame.getContentPane();
        frame.setTitle("Animation Introduction");

        // default layout is border layout
        cp.add(animationCanvas, BorderLayout.CENTER);
        cp.add(button, BorderLayout.SOUTH);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    

    private class ButtonListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            animationCanvas.getCircle().moveH(10);
            animationCanvas.repaint();
        }
    }



}