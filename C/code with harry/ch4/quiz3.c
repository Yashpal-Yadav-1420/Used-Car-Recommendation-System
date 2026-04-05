/*Write a program to print frist 'n' natural numbers using for loop.*/
#include <stdio.h>

int main(){
    int n, i;
    printf("Enter n :");
    scanf("%d", &n);
    for (i=1;i<=n;i++){
        printf("%d\n",i);
    }
    return 0;
}