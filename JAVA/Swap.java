package JAVA;

import java.util.Scanner;

public class Swap {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Swapping Station\n");
        System.out.print("Enter your number: ");
        int firstNum = input.nextInt();
        System.out.print("Enter your second number: ");
        int secondNum = input.nextInt();
        int a = firstNum;
        firstNum = secondNum;
        secondNum = a;
        System.out.println("The value of firstNum is: "+ firstNum);
        System.out.print("The value of secondNum is: "+ secondNum);
    }
}
