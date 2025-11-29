#include <iostream>
using namespace std;

void printNToOne(int i, int n) {
    // Base case
    if (i > n) {
        return;
    }
    
    // Recursive call first (backtrack)
    printNToOne(i + 1, n);
    
    // Print while returning (backtracking)
    cout << i << " ";
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    cout << "Printing from " << n << " to 1 (using backtrack): ";
    printNToOne(1, n);
    cout << endl;
    
    return 0;
}
