#include <iostream>
using namespace std;

void printNToOne(int n) {
    // Base case
    if (n == 0) {
        return;
    }
    
    // Print current number
    cout << n << " ";
    
    // Recursive call
    printNToOne(n - 1);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    
    cout << "Printing from " << n << " to 1: ";
    printNToOne(n);
    cout << endl;
    
    return 0;
}
