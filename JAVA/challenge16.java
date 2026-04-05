package JAVA;

import java.util.Scanner;

public class challenge16 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your number: ");
        int n = input.nextInt();
        if(n%2==0){
            System.out.print("Entered number is even");
        }
        else{
            System.out.print("Entered number is odd");
        }
    }
}
