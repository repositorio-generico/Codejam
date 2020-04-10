#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tests=0; tests<t; tests++){
        int N;
        cin >> N;
        string lyd;
        cin  >>lyd;
        string ans;
        string path;
        for (int i=0;i< 2*N-2; i++){
            if (lyd[i]=='E'){
                path+='S';
            }
            else path+='E';
        }
        cout << "Case #"<< tests+1<< ": "<<path << endl;
    }
    return 0;
}
