#include <stdio.h>

int main(){
    int number;
    printf("Enter the three numbers: ");
    scanf("%d %d %d", &number, &number, &number);
    while (number>0)
    {
        printf("The maximum of the three numbers is %d .",number);
    break;
    }
    while (number<0)
    {
        printf("The minimum of the three numbers is %d .",number);
    break;
    }
    

    return 0;
}
/*#include <stdio.h>

int main() {
    int num, max, min;

    // Initialize max and min
    max = -2147483648; // Minimum value for an int
    min = 2147483647;  // Maximum value for an int

    // Taking input from the user
    printf("Enter three numbers:\n");

    for (int i = 0; i < 3; i++) {
        scanf("%d", &num);

        // Update max and min
        if (num > max) {
            max = num;
        }
        if (num < min) {
            min = num;
        }
    }

    // Displaying the results
    printf("The maximum of the three numbers is %d.\n", max);
    printf("The minimum of the three numbers is %d.\n", min);

    return 0;
}*/
