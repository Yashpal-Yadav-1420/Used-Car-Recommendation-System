/*Write a program to print multiplication tabke of a given number n.*/
#include <stdio.h>

int main(){
    int n,m,i ;
    printf("Enter n:");
    scanf("%d", &n);
    for (m=1; m < 15; m++)
    {
        i= m*n;
        printf("%d X %d = %d\n",n, m, i);
    }
    
    return 0;
}