/* Write a program to convert lowercase letters to uppercase letters. The program should continue until the user enters EOF. 
by suing infinite loop*/
#include<stdio.h>
int main(void){
    int c;
    for(;;){
        c=getchar();
        if (c==EOF)break;
        if ((c>='a')&&(c<='z'))
        c+='A'-'a';
        putchar(c);
            }
            return 0;
}


