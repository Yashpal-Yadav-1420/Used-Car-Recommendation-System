package JAVA;

import java.util.Scanner;

public class challenge28 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to table creator\n");
        System.out.print("Aapko kiska table print karvana hai: ");
        int n = input.nextInt();
        int a = 1;
        while (a<= 10) {
            int b = n*a;
            String mul = String.format("The Product of %d X %d = ",n,a);
            System.out.println(mul + b);
            a++;
        }
        
    }
}
