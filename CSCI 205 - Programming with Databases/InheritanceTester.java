public class InheritanceTester {
    
    public static void main(String[] args) {
        SavingsAccount mary = new SavingsAccount(3.0);
        mary.deposit(1000);
        System.out.println("Balance: " + mary.getBalance());
        mary.addInterest();
        System.out.println("Balance: " + mary.getBalance());

    }
}



