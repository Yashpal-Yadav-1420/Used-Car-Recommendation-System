/*Repeat 8 code using wkile loop.*/
#include <stdio.h>

int main(){
    int i = 1, n,product = 1;
    printf("Enter n: ");
    scanf("%d", &n);
    while (i<=n)
    {
         product*=i; i++;
         }
         printf("The value of %d! is %d",n,product);
    
    return 0;
}