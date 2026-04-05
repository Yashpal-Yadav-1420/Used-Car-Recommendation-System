/*Write a program to print frist n natural number using do-while loop.*/
#include <stdio.h>

int main(){
    int n, i = 1;
    printf("Enter n:");
    scanf("%d", &n);
      do{
        printf("%d\n", i); i++;
      }
      while (i<=n);
    return 0;
}