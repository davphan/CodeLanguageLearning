#include <iostream>
using namespace std;

void checkPalindrome() {
  int original, in_num, final_num, temp_digit = 0;

  cout << "Enter a positive number: ";
  cin >> in_num;

  original = in_num;
  do {
    temp_digit = in_num % 10;
    final_num = final_num * 10 + temp_digit;
    in_num = in_num / 10;
  } while (in_num != 0);

  cout << "Reversed num: " << final_num << endl;

  if (original == final_num) {
    cout << "Palindrome!";
  } else {
    cout << "Not a palindrome...";
  }
}

int main() {
  checkPalindrome();
  return 0;
}