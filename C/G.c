//#include <stdio.h>
//#include <math.h>

//int main() {
    //double a = 2, b = 7, c = 2;
    //double discriminant, x1, x2;

    // Calculate the discriminant
    //discriminant = (b * b) - 4 * a * c;

    // Check if discriminant is non-negative
    //if (discriminant >= 0) {
        // Calculate the two roots using the quadratic formula
       // x1 = (-b + sqrt(discriminant)) / (2 *a);
       // x2 = (-b - sqrt(discriminant))/ (2 *a);

        // Print the roots
        //printf("Value of x1: %.5lf\n", x1);
        //printf("Value of x2: %.5lf\n", x2);
    //} //else {
        // If the discriminant is negative, the roots are complex
        //printf("The roots are complex.\n");
    //}
    
    

    //return 0;
//}

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t sem;   /* binary semaphore, init = 0 */

void *P1(void *arg) {
    /* --- S1 instructions --- */
    printf("  P1 -> S1 started\n");
    sleep(1);
    printf("  P1 -> S1 completed\n");

    sem_post(&sem);   /* SIGNAL: unlock P2 */
    printf("  P1 -> semaphore released (signal)\n");
    return NULL;
}

void *P2(void *arg) {
    printf("  P2 -> waiting on semaphore (wait)...\n");
    sem_wait(&sem);   /* WAIT: block until P1 signals */

    /* --- S2 instructions --- */
    printf("  P2 -> S2 started\n");
    sleep(1);
    printf("  P2 -> S2 completed\n");
    return NULL;
}

int main(void) {
    pthread_t t1, t2;
    sem_init(&sem, 0, 0);   /* init value = 0 (locked) */

    for (int i = 1; i <= 5; i++) {
        printf("\n-- Run %d --\n", i);

        pthread_create(&t1, NULL, P1, NULL);  // Create P1 first
        pthread_create(&t2, NULL, P2, NULL);  // Create P2 after P1

        pthread_join(t1, NULL);
        pthread_join(t2, NULL);

        printf("-- Run %d done\n", i);
    }

    sem_destroy(&sem);
    return 0;
}