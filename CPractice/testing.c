#include <stdio.h>

#define ASCII_NUM 48

void formatTime(int time, char * buffer);

int main() {
  char buf[12] ="__:__:__:_0";
  formatTime(44639, buf);
  // char s[10] = "hello";
  // int num = 4;
  // s[0] = num + 48;
  // printf("%s\n", s);
}

void formatTime(int time, char * buffer) {
  printf("Entering Format Time func\n");
  // Hours
  printf("Hours 1: %d\n", time / 10 / 60 / 60 / 10);
  buffer[0] = time / 10 / 60 / 60 / 10 + ASCII_NUM;
  printf("Hours 1: %d\n", time / 10 / 60 / 60 % 10);
  buffer[1] = time / 10 / 60 / 60 % 10 + ASCII_NUM;
  printf("%s\n", buffer);

  // Minutes
  time %= 10 * 60 * 60;
  printf("Minutes 1: %d\n", time / 10 / 60 / 10);
  buffer[3] = time / 10 / 60 / 10 + ASCII_NUM;
  printf("Minutes 0: %d\n", time / 10 / 60 % 10);
  buffer[4] = time / 10 / 60 % 10 + ASCII_NUM;
  printf("%s\n", buffer);

  // Seconds
  time %= 10 * 60;
  printf("Seconds 1: %d\n", time / 10 / 10);
  buffer[6] = time / 10 / 10 + ASCII_NUM;
  printf("Seconds 0: %d\n", time / 10 % 10);
  buffer[7] = time / 10 % 10 + ASCII_NUM;
  printf("%s\n", buffer);

  // 10th seconds
  time %= 10;
  printf("10th seconds: %d\n", time);
  buffer[9] = time + ASCII_NUM;
  printf("%s\n", buffer);
}