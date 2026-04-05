/* write a program to sum frist ten natural numbers using while loop.*/
#include <stdio.h>

int main(){
    int i = 1, sum = 0;
    while (i<=10)
    {
        sum+=i;i++;
    }
    printf("The sum of frist 10 natural numbers is %d",sum);
    return 0;
}
