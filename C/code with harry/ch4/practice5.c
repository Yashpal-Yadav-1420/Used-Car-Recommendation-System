/*write a program to calculate the sum of the numbers occuring in the multiplication table of 8.*/
#include <stdio.h>

int main(){
    int i,sum=0;
    for (i = 1; i <= 10; i++)
    {
        sum +=(i*8);
    }
         printf("The sum of multiples of 8 is %d", sum);
    
    return 0;
}