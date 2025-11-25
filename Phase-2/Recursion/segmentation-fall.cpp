#include <iostream>
using namespace std;

//  This function will cause a segmentation fault due to infinite recursion

void f(){
    cout << 1 << endl;
    f();
}

int main()
{
    f();
    return 0;
}