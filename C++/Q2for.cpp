/*Check if number is prime or not*/
# include<iostream>
using namespace std;

int main(){
    int n;
    int i;
    cout << "Enter n: ";
    cin >> n;
    for ( i = 2; i <= n - 1; i++)
    {
      if(n%i == 0){
        cout << "It is not a prime";
        break;
      }else{ 
        cout << "It is a prime number";
        break;
      }
    }
    
   

    return 0;
}   