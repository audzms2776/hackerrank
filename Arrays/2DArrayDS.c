#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the hourglassSum function below.
int hourglassSum(int arr_rows, int arr_columns, int** arr) {
    int max = -1000000;
    
    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            int temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] 
                + arr[i+1][j+1] 
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
            
            if (temp > max){
                max = temp;
            }
        }
    }
    
    return max;
}
