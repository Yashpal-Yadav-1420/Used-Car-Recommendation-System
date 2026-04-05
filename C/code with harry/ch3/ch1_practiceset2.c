/*calculate the area of circle and modify the same program to calculate the volume of a cylinder given its raidus and height
*/
#include <stdio.h>

int main(){
    int r = 6;
    int height = 10;
    printf("The area of circle with raidus %d is %f", r, 3.14*r*r);
    printf("The volume of cylinder with raidus %d and height %d is %f", r, height, 3.14*r*r*height);
    
    return 0;
}