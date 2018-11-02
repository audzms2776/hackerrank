#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <map>

// https://www.acmicpc.net/problem/2108

using namespace std;

int main() {
    int num = 0;
    cin >> num;

    vector<int> v;
    map<int, int> num_map;
    int sum=0;

    for (int i=0; i<num; ++i) {
        int temp_int = 0;
        cin >> temp_int;

        sum += temp_int;
        
        if (num_map[temp_int]) {
            ++num_map[temp_int];
        } else {
            num_map[temp_int] = 1;
        }

        v.push_back(temp_int);    
    }

    sort(v.begin(), v.end());
    int min_num = v[0];
    int max_num = v[v.size() - 1];
    int middle_num = v[v.size() / 2];

    // http://hyeonstorage.tistory.com/329
    map<int, int>::iterator iter;
    int max_key = 0, max_value = -1;

    for (iter = num_map.begin(); iter != num_map.end(); ++iter) {
        int k = (*iter).first;
        int v = (*iter).second;

        if (v > max_value) {
            max_key = k;
            max_value = v;
        }

        // cout<< k<<v<<endl;
    }

    vector<int> v2;

    for (iter = num_map.begin(); iter != num_map.end(); ++iter) {
        int k = (*iter).first;
        int v = (*iter).second;

        if (v == max_value) {
            v2.push_back(k);
        }
    }

    sort(v2.begin(), v2.end());

    if (v2.size() > 1) {
        max_key = v2[1];
    } else {
        max_key = v2[0];
    }

    cout << floor(float(sum) / v.size() + 0.5) << endl;
    cout << middle_num <<endl;
    cout << max_key << endl;
    cout << max_num - min_num << endl;
}
