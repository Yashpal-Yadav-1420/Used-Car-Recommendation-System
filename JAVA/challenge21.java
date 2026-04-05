package JAVA;

import java.util.Scanner;

public class challenge21 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your first number: ");
        int n = input.nextInt();
        System.out.print("Enter your second number: ");
        int a = input.nextInt();
        int s = a&n;
        System.out.print("\nOutput " + s );
    }
}
