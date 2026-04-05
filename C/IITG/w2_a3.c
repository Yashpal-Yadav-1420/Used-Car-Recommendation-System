#include <stdio.h>

int main(){
    int i, j, k;
    printf("Enter the frist angle: ");
    scanf("%d", &i);
    printf("Enter the second angle: ");
    scanf("%d", &j);
    k = 180 - (i+j);
    printf("The third angle is %d degree",k);
    return 0;
}