/*#include<stdio.h>
int main(){
    printf("hello world and yashpal");
    return 0;
}
#include<stdio.h>
int main()

{

    int A[2][4] = {{1,3,5,7}, {1,2,9}};

    printf("%d", A[1][3]);
    return 0;

}*/
/*#include <stdio.h>
int factorial(int);
int n  = 6;
main(){
    int fac;
    fac = factorial(n)
    printf("The factorial is %d", fac)
}
int factorial(int n){
    int fac = 1;
    while (n >= 1){
        fac = fac*n;
        n = n-1
    }
}*/

#include <stdio.h>
#define MAX 100


void printArray(int A[], int n);


// Counting Sort function
void countingSort(int A[], int n) {
 int output[n]; // Output array
 int count[MAX] = {0}; // Count array initialized to 0
 int i;


 // Step 1: Find the maximum value in A[]
 int max = A[0];
 for (i = 1; i < n; i++) {
 if (A[i] > max)
 max = A[i];
 }


 // Step 2: Construct the count array
 for (i = 0; i < n; i++)
 count[A[i]]++;


 printf("\nCount array before cumulative sum:\n");
 printArray(count, max + 1);


 // Step 3: Convert count array to cumulative sum array
 for (i = 1; i <= max; i++)
 count[i] += count[i - 1];


 printf("\nCount array after cumulative sum:\n");
 printArray(count, max + 1);


 // Step 4-7: Place elements into output array in stable order
 for (i = n - 1; i >= 0; i--) {
 int pos = count[A[i]];
 pos = pos - 1;
 output[pos] = A[i];
 count[A[i]]--;
 }


 // Step 8: Copy sorted output back to original array A
 for (i = 0; i < n; i++)
 A[i] = output[i];
 printf("\nCumulative Count array after sorting (used for positions, now decremented):\n");
 printArray(count, max + 1);
}