#include <assert.h>
#include <iostream>
#include <vector>
typedef std::vector<std::vector<int>> matrix;

void rotate(matrix& image) {
    int rows = image.size() - 1;
    int cols = image[0].size() - 1;

    int start = 0;
    int end = image.size() - 1;
    int level = 0;
    while(true) {
        if(start >= end) {
            break;
        }

        for(int i = start; i < end; i++) {
            int temp = image[level][i];
            image[level][i] = image[rows-level][i];
            image[rows-level][i] = image[rows-level][cols-i];
            image[rows-level][cols-i] = image[level][cols-i];
            image[level][cols-i] = temp;
        }

        start++;
        end--;
    }
}

int main() {
    matrix image = {
            {1, 2},
            {3, 4}
    };
    matrix rotated = {
            {3, 1},
            {4, 2}
    };

    rotate(image);
    assert(image == rotated);
}
