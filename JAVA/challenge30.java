package JAVA;

import java.util.Scanner;

public class challenge30 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Factorial Calculator\n");
        System.out.print("Enter your number: ");
        int n = input.nextInt();
        /*int a = 1;
        int b = 1; 
        while (n>=a) {
            b *=a ;
            a++;
        }
        System.out.println("The product of " + n +" Factorial is: "+b);*/
        long fact = factorial(n);
        System.out.println("Factorial is: " + fact);
    }
    public static long  factorial(int n) {
        if (n < 2){
            return 1;
        }
        long fact = 1;
        int i = 2;
        while (i <= 2) {
            fact *=i;
            i++;
        }
        return fact;
        
    }
}
