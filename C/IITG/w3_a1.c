/*#include <stdio.h>

int main(){
    int i = 1, sum = 0 ;
    scanf("%d", &sum);
      while (i<=10)
      { if (i == 3*i){
        i++;
        continue;
      }
        sum+=i;
        printf("%d",i);
        i++;
      }
      printf("The sum of series is %d .", sum );
    return 0;
}
#include <stdio.h>

int main(){
    int i,N;
    printf("Enter the value of N: ");
    scanf("%d",&N);
    for ( i = 1; i <=10 ; i++)
    {
        N+=i;
        printf("The value of this series is %d .", N);
        if(N%3 ==0)
        continue;
    }
    
    return 0;
}*/
#include <stdio.h>

int main() {
    int N, sum = 0;

    // Taking input from the user
    printf("Enter the value of N: ");
    scanf("%d", &N);

    // Calculating the sum of all numbers from 1 to N except multiples of 3
    for (int i = 1; i <= N; i++) {
        if (i % 3 != 0) {
            sum += i;
        }
    }

    // Displaying the result
    printf("The sum of this series is %d .", sum);

    return 0;
}


