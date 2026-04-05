#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t S, Q;

void *P0(void *arg) {
    printf("P0: acquiring S...\n"); fflush(stdout);
    sem_wait(&S);
    printf("P0: acquiring Q...\n"); fflush(stdout);
    sem_wait(&Q);               /* same order as P1: S -> Q */

    printf("P0: holding S and Q — doing work\n"); fflush(stdout);

    sem_post(&Q);
    sem_post(&S);
    printf("P0: released both semaphores\n"); fflush(stdout);
    return NULL;
}

void *P1(void *arg) {
    printf("P1: acquiring S...\n"); fflush(stdout);
    sem_wait(&S);               /* same order as P0: S -> Q */
    printf("P1: acquiring Q...\n"); fflush(stdout);
    sem_wait(&Q);

    printf("P1: holding S and Q — doing work\n"); fflush(stdout);

    sem_post(&Q);
    sem_post(&S);
    printf("P1: released both semaphores\n"); fflush(stdout);
    return NULL;
}

int main(void) {
    pthread_t t0, t1;
    sem_init(&S, 0, 1);
    sem_init(&Q, 0, 1);

    printf("=== Fixed Demo: P0(S->Q)  P1(S->Q) — no circular wait ===\n");
    pthread_create(&t0, NULL, P0, NULL);
    pthread_create(&t1, NULL, P1, NULL);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    sem_destroy(&S);
    sem_destroy(&Q);
    printf("=== Both processes completed successfully ===\n");
    return 0;
}
