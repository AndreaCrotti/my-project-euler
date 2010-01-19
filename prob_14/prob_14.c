// -*- compile-command: "gcc -o prob_14 prob_14.c" -*-

#include "stdio.h" 
#include "limits.h" 
#define N 1000000

unsigned int memory[N]; 
long long int collatz_cycle_len(long long int n) { 
    if (n < N && memory[n]) 
        return memory[n]; 
    long long int result; 
    if (n == 1) 
        result = 1; 
    else if (n & 1) 
        result = collatz_cycle_len(3*n + 1) + 1; 
    else 
        result = collatz_cycle_len(n / 2) + 1; 
    if (n < N && result < ULONG_MAX) 
        memory[n] = result; 
    return result; 
} 

int main() { 
    int i; 
    int max = 0; 
    for (i = 1; i < N; i++) { 
        int r = collatz_cycle_len(i); 
        if (r > max) 
            max = r; 
    } 
    printf("%d\n", max); 
    return 0; 
} 
