/*Quiz: Write a program to find grade of a student given his marks based on below
90-100=> A
80-90=>B 
70-80=>C  
60-70=>D
50-60=>E
<50   =>F*/

#include <stdio.h>

int main(){
    float Marks;
    char grades;
    printf("Enter your Marks:");
    scanf("%f",&Marks);
    if(Marks<=100 && Marks>= 90){
        printf("Your grades = A");}

        else if(Marks<=90 && Marks>= 80){
        printf("Your grades = B");}

        else if(Marks<=80 && Marks>= 70){
        printf("Your grades = C");}

        else if(Marks<=70 && Marks>= 60){
        printf("Your grades = D");}

        else if(Marks<=60 && Marks>= 50){
        printf("Your grades = E");}

        else{
            printf("Your grades = F");
            }
             
    return 0;
}