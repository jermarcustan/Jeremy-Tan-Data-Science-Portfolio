public class Ticket {
    
    private String type;
    private double ticket_value;

    public Ticket(double c) {
        if (c == 500) {
            type = "All Access Ticket";
            ticket_value = c;
        }
        else {
            type = "Single Access Ticket";
            ticket_value = c;
        }

    }

    public double getCredit() {

        return ticket_value;
    }

    public boolean isAllAccess() {

        if (type == "All Access Ticket") {
            return true;
        }
        else {
            return false;
        }
    }
    public void updateCredit(double amt) {

        ticket_value = amt;
        
    }
}
