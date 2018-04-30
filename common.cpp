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
