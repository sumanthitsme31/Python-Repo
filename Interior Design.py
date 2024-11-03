import java.util.Scanner;
public class Interior{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x1=sc.nextInt();
        int y1=sc.nextInt();
        int x2=sc.nextInt();
        int y2=sc.nextInt();
        int t1=x1+y1;
        int t2=x2+y2;
        int min=Math.min(t1,t2);
        System.out.println(min);
    }
}