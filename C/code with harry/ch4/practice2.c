/* Write a program to print multiplication table of 10 in reversr order.*/
#include <stdio.h>

int main(){
    int i,n ;
    i = 10;
    for (n=10; n>0 ; n--){
        printf("%d X %d = %d\n",i, n, i*n);

    }   
    return 0;
}