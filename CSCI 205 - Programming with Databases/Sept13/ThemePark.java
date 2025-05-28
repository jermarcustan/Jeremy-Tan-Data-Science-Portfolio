public class ThemePark {
	
	public static void main( String[] args ) {
		
		// place your code here
		TicketScanner[] ts;
		ts = new TicketScanner[5];
		Attraction[] atn;
		atn = new Attraction[3];
		Ticket[] tks;;
		tks = new Ticket[25];
		
		/*
			This loop creates multiple instances of Ticket
			and places them in the array of Tickets.
			STUDENTS MUST NOT EDIT THIS CODE.
		*/
		for( int i = 0; i < tks.length; i++ ) {
			if( i % 4 == 0 )
				tks[i] = new Ticket( 500.00 );
			else if( i % 4 == 1 )
				tks[i] = new Ticket( 49.49 );
			else if( i % 4 == 2 )
				tks[i] = new Ticket( 81.81 ); 
			else
				tks[i] = new Ticket( 125.25 );	
		}
		
		// Create the TicketScanner and Attraction objects

		for (int i = 0; i <ts.length; i++) {
			ts[i] = new TicketScanner();
		}

		atn[0] = new Attraction("Roller Coaster", 125.25);
		atn[1] = new Attraction("Ferris Wheel", 81.81);
		atn[2] = new Attraction("Carousel", 49.49);

		
		/*
			This loop performs multiple scanTicket operations on
			specific TicketScanners.
			All tickets are scanned in this loop.
			STUDENTS MUST NOT EDIT THIS CODE.
		*/
		for( int i = tks.length-1; i >= 0; i-- )
			ts[i%ts.length].scanTicket( atn[i%atn.length], tks[i] );
		
		/*
			This loop performs multiple scanTicket operations on
			specific TicketScanners.
			Only the all-access tickets are scanned again in this loop.
			STUDENTS MUST NOT EDIT THIS CODE.
		*/
		for( int i = 0; i < tks.length; i++ ) {
			if( tks[i].isAllAccess() )
				ts[i%ts.length].scanTicket( atn[i%atn.length], tks[i] );
		}
		
		System.out.println("----------------- MY THEME PARK SALES REPORT -----------------");
        System.out.println("| Scanner | Collection | SAT | AAT | REJECT | RC | FW | CL |");
        System.out.println("--------------------------------------------------------------");
		for (int i = 0; i < ts.length; i++ ){
			System.out.printf(String.format("| Scanner %d | PHP %.2f | %d | %d | %d | %d | %d | %d |\n", i+1, ts[i].getCollections(), ts[i].getSingleAccess(), ts[i].getAllAccess(), ts[i].getRejects(), ts[i].getRollerCoaster(), ts[i].getFerrisWheel(), ts[i].getCarousel() ));
		}
        System.out.println("--------------------------------------------------------------");
		
		

	}
	
}