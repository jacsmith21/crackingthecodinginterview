#include <assert.h>
#include <map>

std::map<char, int>* bucket(std::string& str) {
  std::map<char, int>* buckets = new std::map<char, int>;
  for(char& c : str) {
    if(buckets->count(c)) {
      (*buckets)[c]++;
    } else {
      (*buckets)[c] = 1;
    }
  }

  return buckets;
}

bool equal(std::map<char, int>* map1, std::map<char, int>* map2) {
  return map1->size() == map2->size() && std::equal(map1->begin(), map1->end(), map2->begin());
}

bool is_permutation(std::string& str1, std::string& str2) {
  return equal(bucket(str1), bucket(str2));
}

int main() {
  std::string str1 = "hello";
  std::string str2 = "llohe";
  std::string str3 = "lllhe";

  assert(is_permutation(str1, str2));
  assert(!is_permutation(str2, str3));
}
