#include <vector>
#include <iostream>

using namespace std;

int divisors(int n){  
    int cnt = 0;
    int dn = 1;
    while(dn <= (n / dn)){
        if(n % dn == 0){
            cnt += n / dn == dn ? 1 : 2;
            cout << "num: " << n << " " << cnt << "\n";
        }
        dn++;
    }
  return cnt;
}

int main()
{
    cout << divisors(1) << "\n";
    cout << divisors(4) << "\n";
    cout << divisors(5) << "\n";
    cout << divisors(12) << "\n";
    cout << divisors(25) << "\n";
    cout << divisors(30) << "\n";
    cout << divisors(4096) << "\n";
};