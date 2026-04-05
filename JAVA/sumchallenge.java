package JAVA;

import java.util.Scanner;

public class sumchallenge {
    public static void main(String[] args) {
       /*  int s = 15;
        int n = 20;
        int a = s + n;
        System.out.print(a);*/
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to our Calculator");
        System.out.print("Please enter your first number: ");
        int firstNum = input.nextInt();
        System.out.print("Please enter the second number: ");
        int secondNum = input.nextInt();
        System.out.println( firstNum + secondNum);
    }
}
