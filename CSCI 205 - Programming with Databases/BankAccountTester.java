public class BankAccountTester {
    
    public static void main(String[] args) {
        BankAccount b1 = new BankAccount();
        BankAccount b2 = new BankAccount();

        b1.deposit(500);
        b2.deposit(1000);

        System.out.println(b1.getBalance());
        System.out.println(b2.getBalance());

    }

}
