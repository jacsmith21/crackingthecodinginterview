#include <string>
#include <assert.h>
#include <iostream>

std::string urlify(std::string& string, int length) {
  int pos = string.size() - 1;
  for(int i = length-1; i >= 0; i--) {
    if(string[i] == ' ') {
      string[pos] = '0';
      string[pos-1] = '2';
      string[pos-2] = '%';
      pos -= 3;
    } else {
      string[pos] = string[i];
      pos--;
    }
  }
  return string;
}

int main() {
  std::string str1 = "h el lo    ";
  int length = 7;

  assert("h%20el%20lo" == urlify(str1, length));
}
