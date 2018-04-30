#include <assert.h>
#include <map>

bool is_unique(std::string& string) {
  std::map<char, bool> map;
  for(char& c : string) {
    if(map.count(c)) {
      return false;
    }

    map[c] = true;
  }

  return true;
}

int main() {
  std::string str1 = "hello";
  std::string str2 = "helo";

  assert(!is_unique(str1));
  assert(is_unique(str2));
}
