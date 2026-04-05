# include<iostream>
using namespace std;

int main(){
    int Number;
    cout << "Enter your number: ";
    cin >> Number;
     if(Number%2 == 0){
        cout << "Number is even\n";
     }else{
        cout << "Number is odd\n";
     }
  return 0;  
}