import java.util.Scanner;
public class Donation{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        String input=sc.nextLine();
        String[] parts=input.split(" ");
        int x=Integer.parseInt(parts[0]);
        int y=Integer.parseInt(parts[1]);
        int donation=y-x;
        System.out.println(donation);
    }
}