package JAVA;

import java.util.Scanner;

public class challenge18 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Leap year calculator\n");
        System.out.print("Enter your Year: ");
        int n = input.nextInt();
        if(n%4==0 && n%100!=0 || (n%400==0)){
            System.out.print("Entered year is a leap year");
        }
        else{
            System.out.print("Entered year is not a leap year");
        }

    }
}
