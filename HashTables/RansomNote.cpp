#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <algorithm>

using namespace std;

// Complete the checkMagazine function below.
void checkMagazine(vector<string> magazine, vector<string> note) {
    int c_map[26] = {0};

    for (int i=0; i<magazine.size(); ++i) {
        const char* s = magazine[i].c_str();
        
        for (int j=0; s[j] != '\0'; ++j) {
            int c_idx = s[j] - 'a';    
            ++c_map[c_idx];
        }
    }
    
    for (int i=0; i<note.size(); ++i) {
        const char* s = note[i].c_str();
        
        for(int j=0; s[j] != '\0'; ++j) {
            int c_idx = s[j] - 'a';    

            if (c_map[c_idx] == 0) {
                cout << "No" <<endl;
                return;
            } else {
                --c_map[c_idx];
            }
        }
    }

    cout<< "Yes" <<endl;
}
