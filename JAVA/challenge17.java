package JAVA;

import java.util.Scanner;

public class challenge17 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a: ");
        int a = input.nextInt();
        System.out.print("Enter b: ");
        int b = input.nextInt();
        System.out.print("Enter c: ");
        int c = input.nextInt();
        if(a>b&&b>c){
            System.out.print("A is the greatestof all three.");
        }
        else if (a<b && b>c){
            System.out.print("B is the greatestof all three.");
        }
        else{
            System.out.print("C is the greatestof all three.");
        }
    }
    
}
