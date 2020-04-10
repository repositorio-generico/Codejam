#include <iostream>
#include <string>

using namespace std;

int t;
string a;
int j=0;
void printn(string k, string fin){
    bool aux=false;
    for (int i=0; i<k.length(); i++){
        if (k[i]!='0') aux=true;
        if (aux) cout << k[i];
    }
    cout << fin;
}

int main() {

    cin >> t;
    for (int i=0; i<t; i++){
        cin >> a;
        string b;
        for (int j=0; j<a.length(); j++){
            if (a[j]=='4'){
                b=b+'2';
                a[j]='2';
            }
            else{
                b=b+'0';
            }
        }
        string ans= "Case #"+std::to_string(i+1)+": ";
        cout << ans;
        printn(a," ");
        printn(b, "\n");
    }
    return 0;
}
