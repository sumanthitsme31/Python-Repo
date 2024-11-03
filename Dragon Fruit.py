import java.util.Scanner;
public class Dragon{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        System.out.println(Divide(x));
    }
    public static String Divide(int x)
    {
    if(x%2==0 && x>=4)
    {
        return "YES";
    }
    else
    {
        return "NO";
    }
    }
}