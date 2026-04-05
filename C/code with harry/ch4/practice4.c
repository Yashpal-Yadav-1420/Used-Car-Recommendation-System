/*Write a program to implement program 5 using 'for' and 'do-while' loop.*/
#include <stdio.h>

int main(){
    int i,sum = 0,f;
    for ( i = 1; i <=10; i++)
    {
      sum+=i;
        
    }
    
    printf("The value of frist ten natural numbers %d\n",sum);
    
    return 0;
}