/*Write a program to determine wether a character entered by the use ris lowercase or not.*/
#include <stdio.h>

int main(){
    char ch = 'D';
    printf("The character is %c\n",ch);
    printf("The value of character is %d\n", ch);

    if (ch>97 && ch<122){
        printf("This character is lower case"); 
    }
    else {
        printf ("This character is upper case");
    }
    return 0;
}