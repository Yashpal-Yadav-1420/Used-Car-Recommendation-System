/* we will write a program that generates a random number and asks the player to guess it. If the  player's */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    srand(time(0));
    int randomnumber = (rand() % 100) + 1;
    int no_of_guesses =  0;
    int guessed;
    //printf("Random Number: %d\n", randomnumber);
    do
    {
    printf("Guess the number");
    scanf("%d",&guessed);
    if (guessed>randomnumber)

    { printf("Lower number please!\n ");}
       else{
        printf("Larger number please!\n");
       }
        
    
    }
     while (guessed!=randomnumber);

    printf("You guessed the number in %d guesses", no_of_guesses);
    
    return 0;
}