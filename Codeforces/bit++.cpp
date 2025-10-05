#include<iostream>
#include<vector>
#include <string>
using namespace std;

int main(){
    int n; cin>> n;
    vector<string> operations(n);

    for(int i=0; i<n; i++){
        cin>> operations[i];
    }

    int x = 0;
    for(auto operation : operations) {
        if(operation.find("+") != string::npos) {
            x++;
        }
        else {
            x--;
        }
    }

    cout<< x<< endl;
}

    // for(int i=0; i<operations.size(); i++) {
    //     if(operations[i].find("+") != string::npos) {
    //         x++;
    //     }
    //     else {
    //         x--;
    //     }
    // }