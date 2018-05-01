#include <assert.h>
#include <string>
#include <iostream>
#define print(x) std::cout << (x) << std::endl

std::string compress(std::string str) {
  int count = 0;
  char prev;
  bool first = true;
  for(char& c : str) {
    if(first || c != prev) {
      count++;
      first = false;
    }

    prev = c;
  }

  std::string compressed(count*2, ' ');

  first = true;
  int position = 0;
  count = 0;
  for(char& c : str) {
    if(!first && c != prev) {
      compressed[position] = prev;
      compressed[position+1] = '0' + count;

      count = 0;
      position += 2;
    }

    prev = c;
    count++;
    first = false;
  }
  compressed[position] = prev;
  compressed[position+1] = '0' + count;

  return compressed;
}

int main() {
  assert(compress("paa") == "p1a2");
  return 0;
}
