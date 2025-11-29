#include <iostream>
using namespace std;

void prinOneToNBacktrack(int i) {
    // Base case
    if (i < 1) {
        return;
    }

    // Recursive call
    prinOneToNBacktrack(i - 1);
    cout << i << " ";
}

int main() {
    int n;
    // cout << "Enter a number: ";
    // cin >> n;
    n = 10;
    cout << "Printing from " << "1 to " << n << ": ";
    prinOneToNBacktrack(n);
    cout << endl;
    
    return 0;
}
