package JAVA;

import java.util.Scanner;

public class challenge19 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your total marks: ");
        int n = input.nextInt();
        double a = n/5;
        if (a>90){
            System.out.print("Your garde is A");
        }else if (a>=75) {
            System.out.print("Your grade is B");
        }else if (a>=60) {
            System.out.print("Your grade is c");
        }else if (a>=30) {
            System.out.print("Your garde is D");
        }else if (a<=30) {
            System.out.print("Your grade is below F");
        }
        
    }
}