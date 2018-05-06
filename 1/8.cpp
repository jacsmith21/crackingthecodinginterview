//
// Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
// column are set to O.
//

#include <assert.h>
#include <numeric>
#include <vector>

typedef std::vector<std::vector<int>> matrix;

void zero(matrix& mat) {
    unsigned long n_rows = mat.size();
    unsigned long n_cols = mat[0].size();

    std::vector<int> cols(n_cols, 0);
    std::vector<int> rows(n_rows, 0);


    for(int i = 0; i < n_rows; i++) {
        for(int j = 0; j < n_cols; j++) {
            if(mat[i][j] == 0) {
                rows[i] = 1;
                cols[j] = 1;
            }
        }
    }

    for(int i = 0; i < n_rows; i++) {
        if(rows[i]) {
            for(int j = 0; j < n_cols; j++) {
                mat[i][j] = 0;
            }
        }
    }

    for(int j = 0; j < n_cols; j++) {
        if(cols[j]) {
            for(int i = 0; i < n_rows; i++) {
                mat[i][j] = 0;
            }
        }
    }
}

int main() {
    matrix mat = {{1, 5, 0}, {0, 4, 7}, {2, 7, 8}};
    zero(mat);
    matrix exp = {{0, 0, 0}, {0, 0, 0}, {0, 7, 0}};
    assert(mat == exp);
}