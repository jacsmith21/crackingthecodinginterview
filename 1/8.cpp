//
// Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
// column are set to O.
//

#include <assert.h>
#include <numeric>

typedef matrix std::vector<std::vector<int>>

void zero(matrix& mat) {
    int n_cols = mat[0].size();
    std::vector<int> range(10);
    std::iota(std::begin(range), std::end(range), 0);
    int n_cols_left = n_cols;
    
    for(int i = 0; i < mat.size(); i++) {
    }
}

int main() {
    assert(true);
}