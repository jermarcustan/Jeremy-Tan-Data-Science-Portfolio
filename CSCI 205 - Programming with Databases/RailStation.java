public class RailStation {

    public static void main(String[] args) {
        TicketGate gate1 = new TicketGate();
        TicketGate gate2 = new TicketGate();
        TicketGate gate3 = new TicketGate();
        gate1.collectFare(true, 180, 115);
        gate2.collectFare(true, 110, 120);
        gate3.collectFare(true, 130, 112);
        gate1.collectFare(false, 0, 114);
        gate2.collectFare(false, 0, 111);
        gate3.collectFare(true, 113, 114);
        gate1.collectFare(false, 0, 110 );
        gate2.collectFare(true, 15, 111);
        gate2.collectFare(true, 17, 113);

        System.out.println("---------- RAIL STATION REPORT ----------");
        System.out.println("|    Gate |    Fares |   SJT |   SVT |   LRB |");
        System.out.println("-----------------------------------------");
        System.out.printf(String.format("| Gate 1 | PHP %.2f | %d | %d | %d |\n", gate1.getCollections(), gate1.getSJT(), gate1.getSVT(), gate1.getBonuses()));
        System.out.printf(String.format("| Gate 2 | PHP %.2f | %d | %d | %d |\n", gate2.getCollections(), gate2.getSJT(), gate2.getSVT(), gate2.getBonuses()));
        System.out.printf(String.format("| Gate 3 | PHP %.2f | %d | %d | %d |\n", gate3.getCollections(), gate3.getSJT(), gate3.getSVT(), gate3.getBonuses()));
        System.out.println("-----------------------------------------");



    }
}