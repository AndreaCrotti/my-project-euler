#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <unistd.h>

/*
  This file will contain some useful data structures and functions
  in C
*/

// Returns a boolean
char is_prime(int);
// returns the factors of a number
void factors(long);
double sqrt(double);
double floor(double);

void factors(long n) {
  // allocating memory doubling every time
  int i;
  int size = 2;
  int count = 0;
  int *result;
  // only 2 at the beginning
  result = (int *)malloc(size * sizeof(int));
  for (i = 1; i < (int)floor(sqrt(n)); ++i) {
    if (n % i == 0) {
      if (count > size) {
	  size *= 2;
	  printf("reallocating more memory\n");
	  result = (int *)realloc(result, size * sizeof(int));
	  // assign to my pointer and increment it
      }
      result[count++] = i;
    }
  }
  for (i = 0; i < count; ++i) {
    printf("for %d: %d\n", i, result[i]);
  }
  // finally free the memory
  printf ("final memory used = %d\n", size );
  free(result);
}

int main(int argc, char *argv[])
{
  factors(atoi(argv[1]));
  return 0;
}

