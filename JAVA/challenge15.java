package JAVA;

import java.util.Scanner;

public class challenge15 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
      System.out.print("Please enter your number: ");
      int var = input.nextInt();
      if(var>0) {
        System.out.print("ENtered number is Positive");
      }
      else if (var<0) {
        System.out.print("Entered number is Negative");
      }
      else{
        System.out.print("Entered number is Zero");
      }
    }
    
}
