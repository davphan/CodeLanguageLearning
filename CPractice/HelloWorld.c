#include <stdio.h>

int main() {
  int x = 1.0 / (400 * 2) / 0.000064;
  int y = (int) x;
  printf("%d\n", x);
  return 0;
}