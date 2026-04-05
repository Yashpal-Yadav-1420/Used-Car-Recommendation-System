package JAVA;

import java.util.Scanner;

public class challenge20 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to gae calculator\n");
        System.out.print("Pleaseenter your age: ");
        int n = input.nextInt();
        if (n<13) {
            System.out.print("You are a child");
        }else if (n<20) {
            System.out.print("You are a Teenager");
        }else if (n<60) {
            System.out.print("You are an adult");
        }else{
            System.out.print("You are a senior citizen");
        }

    }
}
