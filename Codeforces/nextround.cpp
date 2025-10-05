#include<iostream>
#include <vector>
using namespace std;

#define vi vector<int>

int main(){
    int n, k; cin>> n>> k;
    vi v(n);
    
    for(int i=0; i<n; i++) {
        cin>> v[i];
    }

    int a = v[k-1];

    int count = 0;
    for(auto i : v) {
        if(i >= a && i != 0) {
            count++;
        }
    }

    cout<< count<< endl;
}

    // vector<string> names = { "Wasik", "Sumaya", "Nakib"};
    // for(auto name : names) {
    //     cout<< name<< " ";
    // }
    // for(int i=0; i<names.size(); i++) {
    //     cout<< v[i]<< " ";
    // }