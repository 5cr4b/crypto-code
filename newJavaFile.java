import java.util.Scanner;

/**
 *
 * @author cr4b
 */
public class ptbac2 {
    public static void main(String[] args) {
        int a, b, c;
        Scanner scan = new Scanner(System.in);
        
        System.out.println("a= ");
        a = scan.nextInt();
        
        System.out.println("b= ");
        b = scan.nextInt();
        
        System.out.println("c= ");
        c = scan.nextInt();
        
        if (a == 0) {    // kiem tra he so
            if (b == 0) {
                System.out.print("phuong trinh vo nghiem");
            } else {
                System.out.println("phuong trinh co 1 nghiem:"+ "x = " + (-c / b));
            }
        }
        
        float d = b*b - 4*a*c;          //tinh delta
        float x1,x2;
        if(d > 0){
           x1 = (float)((-b + Math.sqrt(d)) / (2*a));
           x2 = (float)((-b - Math.sqrt(d)) / (2*a));
           System.out.print("phuong trinh co nghiem la:"+ "x1:"+ x1+ "va x2 :" + x2 );
        }
        else if(d == 0){
            x1 = (-b / (2*a));
            System.out.print("phuong trinh co nghiep kep :"+x1);
        }
        else{
            System.out.print("phuong trinh vo nghiem");
        }
        
        
        
                
            
    } 
}