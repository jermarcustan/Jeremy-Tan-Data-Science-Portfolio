import javax.swing.JFrame; 
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.Container;
import java.awt.BorderLayout;
import javax.swing.JTextArea;
import java.awt.GridLayout;

// Import the Swing JFrame Class
// JFrame object is the window containing all the buttons and text fields

public class GuiDemo {

    private JFrame frame;
    private JLabel label;
    private JTextField input;
    private JButton button1;
    private JButton button2;
    private JButton button3;
    private int width;
    private int height;
    private JTextArea ta;

    public GuiDemo(int w, int h) {
        frame = new JFrame();
        label = new JLabel("Hello");
        input = new JTextField(10);
        ta = new JTextArea("Hello. \nThis is JTextArea.");
        button1 = new JButton("Button 1");
        button2 = new JButton("Button 2");
        button3 = new JButton("Button 3");
        width = w;
        height = h;
    }

    public void setUpGUI() {
        Container cp = frame.getContentPane();
        GridLayout grid = new GridLayout(2,3);
        cp.setLayout(grid);
        frame.setSize(width, height); // set size of the JFrame
        frame.setTitle("GUI Demo");
        cp.add(input);
        cp.add(ta);
        cp.add(button1);
        cp.add(button2);
        cp.add(label);
        cp.add(button3);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public void setUpButtonListeners() {
        ActionListener buttonListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {
                Object o = ae.getSource();
                if(o == button1) {
                    String s = input.getText();
                    label.setText(s);
                    input.setText("");
                }
                else if(o == button2) {
                    String val = input.getText();
                    double n = Double.parseDouble(val);
                    double result = n * 2;
                    label.setText(Double.toString(result));
                }
            }
        };
        button1.addActionListener(buttonListener);
        button2.addActionListener(buttonListener);
    }

}

