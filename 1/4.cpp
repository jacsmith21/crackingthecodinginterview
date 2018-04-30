#include <assert.h>
#include <map>

std::map<char, int> bucketize(std::string& str) {
  std::map<char, int> buckets;
  for(char& c : str) {
    if(buckets.count(c)) {
      buckets[c]++;
    } else {
      buckets[c] = 1;
    }
  }

  return buckets;
}

bool odd(int n) {
  return n % 2 == 1;
}

bool palindrome_permutation(std::string str) {
  auto buckets = bucketize(str);

  bool found_odd = false;
  for(auto& bucket : buckets) {
    if(odd(bucket.second)){
      if(!found_odd) {
        found_odd = true;
      } else {
        return false;
      }
    }
  }

  return true;
}

int main() {
  std::string str = "h ol lo    ";
  assert(palindrome_permutation("sdfsdff"));
  assert(!palindrome_permutation("sdfsdfft"));
}
