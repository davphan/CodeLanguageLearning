#include <stdio.h>
#include <math.h>

int main() {
  double l1;
  double l2;
  double l3;

  printf("Solving for the hypotenuse of a right triangle.\n\nLength of side 1: ");
  scanf("%lf", &l1);
  printf("Length of side 2: ");
  scanf("%lf", &l2);

  l3 = sqrt(pow(l1, 2) + pow(l2, 2));

  printf("Hypotenuse length: %lf\n", l3);

  return 0;
}