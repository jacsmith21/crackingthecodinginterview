//
// Assume you have a method isSubst ring which checks if one word is a substring
// of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
// call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
//
#include <string>
#include <cassert>

/**
 * Checks is str1 is a substring of str2.
 *
 * @param str1
 * @param str2
 * @return
 */
bool is_substring(std::string& str1, std::string& str2) {
    if(str1.size() > str2.size()) {
        return false;
    }

    int pos = 0;
    for(char& c : str2) {
        if(pos == str1.size()) {
            return true;
        }
        if(c == str1[pos]) {
            pos++;
        } else {
            pos = 0;
        }
    }

    return false;
}

bool rotation(std::string& str1, std::string& str2) {
    if(str1.size() != str2.size()) {
        return false;
    }
    unsigned long length = str1.size();

    int pos = 0;
    for(char& c : str2) {
        if(c == str1[pos]) {
            pos++;
        } else {
            pos = 0;
        }
    }

    if(pos == 0) {
        return false;
    }

    unsigned long end = length - pos - 1;
    std::string slice = str2.substr(0, end);
    return is_substring(slice, str1);
}

int main() {
    std::string str1 = "waterbottle";
    std::string str2 = "erbottlewat";
    std::string str3 = "erobttlewat";
    assert(rotation(str1, str2));
    assert(not rotation(str1, str3));
}

