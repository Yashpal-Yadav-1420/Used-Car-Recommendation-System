#include<stdio.h>

int main() {
    /*int a = 1;
    do {
        printf("Hello World!");
    } while(++a);*/
    for (int i = 0; i < 10; i++) {
    if (i == 5) {
        continue;  // Skip the rest of this iteration when i is 5
    }
    printf("%d ", i);
}

return 0;

}

