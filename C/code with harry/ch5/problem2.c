#include <stdio.h>
float temp (float);

float temp (float c){
    return  (9*c)/5+32;
}
int main(){
    printf("Celcius to Farenhiet for %f ");
    return 0;
}