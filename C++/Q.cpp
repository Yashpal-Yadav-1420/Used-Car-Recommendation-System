/* Find character lowercase or uppercase*/
#include<iostream>
using namespace std;
int main(){
    char Character;
    cout << "Enter character: ";
    cin >> Character;

    if(Character>= 'a' && Character<= 'z'){
        cout << "Character is small\n";
    }else{
        cout << "Character is greater\n";
    }

    return 0;
}