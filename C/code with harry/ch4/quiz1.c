/*Write a program to print natural number from 10 to 20 when initial loop counter is initiliazed to 0.
#include <stdio.h>

int main(){
    int i = 10;
    while (i<=20){
        printf("The value of i is %d \n", i); 
        i++; }     
        ;
    return 0;
}*/

#include <stdio.h>

int main(){
    int i = 10;
    while (i>=10 && i<=20){
        printf("The value of i is %d\n",i); i++;
    }
    return 0;
}