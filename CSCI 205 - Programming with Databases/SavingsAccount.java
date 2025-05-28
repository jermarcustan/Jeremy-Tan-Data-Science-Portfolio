public class SavingsAccount extends BankAccount {
    private double interestRate;

    public SavingsAccount() {
        interestRate = 1.0;
    }

    // default constructor
    public SavingsAccount(double aRate) {
        interestRate = aRate;
    }

    public void addInterest() {
        double interest = getBalance() * interestRate / 100;
        deposit(interest);
    }
}
