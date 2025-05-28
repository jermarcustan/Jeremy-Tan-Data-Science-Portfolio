
public class TicketScanner {

    private double collections;
    private int single_access_tickets;
    private int all_access_tickets;
    private int reject_tickets;
    private int roller_coaster;
    private int ferris_wheel;
    private int carousel;

    public TicketScanner() {
        collections = 0;
        single_access_tickets = 0;
        all_access_tickets = 0;
        reject_tickets = 0;
        roller_coaster = 0;
        ferris_wheel = 0;
        carousel = 0;
    }
    public void scanTicket(Attraction a, Ticket t) {
        if (t.getCredit() >= a.getCost()) {
            collections += a.getCost();

            if (a.getName() == "Roller Coaster") {
                System.out.println("Enjoy your ride on the Roller Coaster.");
                roller_coaster += 1;
            }

            if (a.getName() == "Ferris Wheel") {
                System.out.println("Enjoy your ride on the Ferris Wheel.");
                ferris_wheel += 1;
            }

            if (a.getName() == "Carousel") {
                System.out.println("Enjoy your ride on the Carousel.");
                carousel += 1;
            }

            if (t.isAllAccess() == true) {
                t.updateCredit(t.getCredit() - a.getCost());
                System.out.printf("You have PHP %.2f remaining.\n", t.getCredit());
                all_access_tickets += 1;
            }

            else {
                single_access_tickets += 1;
            }

        }

        else {
            reject_tickets += 1;

            if (a.getName() == "Roller Coaster") {
                System.out.println("Ticket rejected. Insufficient credit for the Roller Coaster.");
            }

            if (a.getName() == "Ferris Wheel") {
                System.out.println("Ticket rejected. Insufficient credit for the Ferris Wheel.");
            }

            if (a.getName() == "Carousel") {
                System.out.println("Ticket rejected. Insufficient credit for the Carousel.");
            }
        }

    }

    public double getCollections() {
        return collections;
    }

    public int getSingleAccess() {
        return single_access_tickets;
    }

    public int getAllAccess() {
        return all_access_tickets;
    }

    public int getRejects() {
        return reject_tickets;
    }

    public int getRollerCoaster() {
        return roller_coaster;
    }

    public int getFerrisWheel() {
        return ferris_wheel;
    }

    public int getCarousel() {
        return carousel;
    }
}
