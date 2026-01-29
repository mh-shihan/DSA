#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout << "Take the length of array: ";
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    // Precompute
    int hash[13] = {0};
    for (int i = 0; i < n; i++)
    {
        hash[arr[i]] += 1;
    }

    int q;
    cout << "Take the number of queries: ";
    cin >> q;
    while (q--){
        int x;
        cout << "Enter the element to be searched: ";
        cin >> x;
        
        // Fetch
        if (x < n && x >= 0){
        cout << "Frequency of " << x << " is " << hash[x] << endl;
        }
        else{
        cout << "Frequency of " << x << " is 0" << endl;
    }
}
}