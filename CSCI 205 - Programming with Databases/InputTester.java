import java.util.Scanner;

public class InputTester
{
   public static void main( String[] args )
   {
     Scanner in = new Scanner(System.in);

     String s1 = in.next();
     String s2 = in.next();
     String s3 = in.next();

     System.out.printf("You entered %s, %s, and %s.\n", s1, s2, s3);
   }
}

