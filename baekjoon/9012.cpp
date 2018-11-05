#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    int num = 0;
    cin >> num;

    for (int i=0; i < num; ++i) {
        string s = "";
        cin >> s;
        bool flag = false;
        
        stack<int> p_stack;

        for (char& c : s) {
            if (c == '(') {
                p_stack.push(1);
            } else {
                if (p_stack.size() > 0 ) {
                    p_stack.pop();
                } else {
                    cout << "NO" << endl;
                    flag = true;
                    break;
                }
            }
        }
        
        if (flag) {
            continue;
        } else if (p_stack.size() != 0) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
}
