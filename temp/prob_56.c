#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int prob_56(int, int);
int sumdigits(int);
void getdigits(int, int *);
double pow(double, double);

int main(int argc, char *argv[])
{
  int *res;
  int i;
  getdigits(1234, res);
  // use log function instead
  // using the array [] notation the step is automatic
  for (i = 0; i < 4; i++ )
    printf("digit %d=%d\n", i, res[i]);
  return 0;
}

// Takes the digit of a number
void getdigits(int n, int *res) {
  int i, j, len;
  len = ((int) floor(log10(n))) + 1;
  printf("len of %d is %d allocating memory now", n, len);
  res = malloc(sizeof(int) * len);

  for (i = len-1; i > 0; i--) {
    j = pow(10, i);
    res[i] = (int) floor(n / j);
    n = n % j;
    printf("now we got n = %d\n", n);
  }
}
