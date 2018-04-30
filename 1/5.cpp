#include <string>
#include <iostream>
#include <assert.h>

bool one_away(std::string str1, std::string str2) {
  int len1 = str1.size();
  int len2 = str2.size();
  int diff = len1 - len2;

  int min;
  if(diff > 1 or diff < -1) {
    return false;
  } else if(len1 > len2) {
    min = len2;
  } else {
    min = len1;
  }

  int i1 = 0;
  int i2 = 0;
  bool incremented = false;
  for(int i = 0; i < min; i++) {
    if(str1[i1] != str2[i2]) {
      if(incremented) {
        return false;
      }

      if(len1 < len2 && !incremented) {
        i2++;
      } else if(len2 < len1 && !incremented) {
        i1++;
      }
      incremented = true;
    }

    i1++;
    i2++;
  }

  return true;
}

int main() {
  assert(one_away("pale", "ple"));
  assert(one_away("pales", "pale"));
  assert(one_away("pale", "bale"));
  assert(!one_away("pale", "bake"));
}
