#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t S, Q;

void *P0(void *arg) {
    printf("P0: acquiring S...\n"); fflush(stdout);
    sem_wait(&S);
    printf("P0: acquired S, now waiting for Q...\n"); fflush(stdout);

    /* --- P1 holds Q and waits for S --- DEADLOCK here --- */
    sem_wait(&Q);

    printf("P0: acquired Q (NEVER REACHED)\n");
    sem_post(&Q);
    sem_post(&S);
    return NULL;
}

void *P1(void *arg) {
    printf("P1: acquiring Q...\n"); fflush(stdout);
    sem_wait(&Q);
    printf("P1: acquired Q, now waiting for S...\n"); fflush(stdout);

    /* --- P0 holds S and waits for Q --- DEADLOCK here --- */
    sem_wait(&S);

    printf("P1: acquired S (NEVER REACHED)\n");
    sem_post(&S);
    sem_post(&Q);
    return NULL;
}

int main(void) {
    pthread_t t0, t1;
    sem_init(&S, 0, 1);
    sem_init(&Q, 0, 1);

    printf("=== Deadlock Demo: P0(S->Q)  P1(Q->S) ===\n");
    pthread_create(&t0, NULL, P0, NULL);
    pthread_create(&t1, NULL, P1, NULL);

    pthread_join(t0, NULL);   /* hangs forever */
    pthread_join(t1, NULL);

    sem_destroy(&S);
    sem_destroy(&Q);
    return 0;
}
