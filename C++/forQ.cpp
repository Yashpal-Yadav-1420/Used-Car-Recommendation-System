# include<iostream>
using namespace std;

int main(){
    int n;
    int i;
    int sum = 0;
    cout << "Enter n: ";
    cin >> n;
    for ( i = 1; i <= n; i++)
    {
      if(i%2 == 0){ // another way to write this is if(i%2 != 0)
        continue;
      }
      sum += i;
    }
    
    cout << "sum = " << sum << endl;

    return 0;
}