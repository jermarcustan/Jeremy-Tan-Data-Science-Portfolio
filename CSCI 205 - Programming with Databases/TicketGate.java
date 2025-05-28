public class TicketGate {
    
    private double total_fare;
    private int sjt_count;
    private int svt_count;
    private int lrb_count;

    public TicketGate() {
        total_fare = 0;
        sjt_count = 0;
        svt_count = 0;
        lrb_count = 0;
    }

    public void collectFare(boolean svt, double svtCredit, double fare) {

        if (svt == true) {

            if (svtCredit < fare) {
            lrb_count += 1;
            total_fare += svtCredit;

            }

            else {
            total_fare += fare;

            }
        svt_count += 1;
        }
        else {
        sjt_count += 1;
        total_fare += fare;


        }
    }

    public double getCollections() {

        return total_fare;

    }

    public int getSJT() {

        return sjt_count;
    }

    public int getSVT() {

        return svt_count;
    }
    public int getBonuses() {

        return lrb_count;
    }

    }


