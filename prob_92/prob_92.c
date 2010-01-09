#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define LIMIT 10000000

int square_digits(int);
int is_89(int);

int main(int argc, char *argv[])
{
  int counter = 0;
  int i;
  for (i = 1; i < LIMIT; i++) {
    //printf("checking %d", i);
    if (is_89(i))
      counter++;
  }
  printf("%d", counter);
}

int square_digits(int i) {
  int res, aux;
  res = 0;
  while (i > 9) {
    aux = i % 10;
    res += aux * aux;
    i = (int) floor(i / 10);
  }
  res += i*i;
  return res;
}

// checks if the chain terminates with 89
int is_89(int n) {
  int next = n;
  while (1) {
    next = square_digits(next);
    if (next == 89)
      return 1;
    if (next == 1)
      return 0;
  }
}
