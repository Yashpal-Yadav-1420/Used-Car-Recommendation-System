package JAVA;

import java.util.Scanner;

public class challenge29 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
       /*  System.out.println("Sum of all the odd numbers\n");
        System.out.print("Enter your number: ");
        int n = input.nextInt();
        int a = 1;
        int b = 0;
        while (a<=n) {
            if (a%2!=0) {
                b +=a ;
            }
            a++;
        }
        System.out.println(b);*/
        System.out.println("Welcome to Odd Sum");
        System.out.print("Please enter your number: ");
        int num = input.nextInt();
        int sum = oddsum(num);
        System.out.print("OddSum till " + num + " is: " + sum);
    }
    public static int oddsum(int num) {
        int sum = 0;
        int i = 1;
        while (i<= num) {
            sum += i;
            i += 2;
        }
        return sum;
    }
}
