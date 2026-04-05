#include <stdio.h>

int main(){
    /*int lenght = 3;
    int breadth = 6;*/
    int lenght, breadth;
    printf("Enter lenght\n");
    scanf("%d", &lenght);
    printf("Enter breadth\n");
    scanf("%d", &breadth);
   
    printf("The area of this rectanglre is %d",lenght*breadth);
    return 0;
}