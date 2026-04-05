/*Sum of numbers from 1 to n.*/
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
      sum += i;
    }
    
    cout << "sum = " << sum << endl;

    return 0;
}