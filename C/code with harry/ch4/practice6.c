/*Write a progrsm to calculate the factorial of a given number using for loop.*/
#include <stdio.h>

int main(){
     int i,n, product = 1;
     printf("Enter n: ");
     scanf("%d", &n);
     for ( i = 1; i <= n; i++)
     {
        product *=i;
     }
        printf("The product of %d! is %d",n, product);

    return 0;
}