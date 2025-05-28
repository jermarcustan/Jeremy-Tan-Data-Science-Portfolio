public class BankAccount {

    private double balance;

    public BankAccount() {
        balance = 0;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance)
            balance = balance - amount;
        else
            System.out.println("Insufficient balance");
    }

    public double getBalance() {
        return balance;
    }

}

