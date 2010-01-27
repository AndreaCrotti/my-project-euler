// -*- compile-command: "gcc -o prob_53 -Wall prob_53.c" -*-
#include <stdio.h>
#include <stdlib.h>

int is_pandig(char *num);
void int_to_digits(int n, int *list);

int main(int argc, char *argv[])
{
  int i;
  int *res = (int *) malloc(sizeof(int) * 3);
  int_to_digits(423, res);
  for (i = 0; i < 3; i++) {
    printf ("digit obtained = %d\n", res[i]);
  }
  free(res);
  return 0;
}

void int_to_digits(int n, int *list) {
  int res, aux, i;
  res = 0, i = 0;

  while (i > 9) {
    aux = i % 10;
    printf ("adding %d\n",aux);
    list[i++] = aux;
    res += aux * aux;
    n /= 10;
  }
}
