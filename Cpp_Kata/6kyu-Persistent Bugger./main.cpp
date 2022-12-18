#include <iostream>
#include <sstream>
#include <iterator>

using namespace std;

int persistence_first_try(long long n){
    int cnt_loop = 0;
    while (n >= 10)
    {
        stringstream ss;
        ss << n;

        int tmp_n = 1;
        for(char& c: ss.str()){
            int c_n = ((int)c - 48);
            tmp_n = tmp_n * c_n;
        }
        n = tmp_n;
        cnt_loop++;
    }
    return cnt_loop;
}

int persistence(long long n) {
    long long p = 1;
    if (n < 10){
        return 0;
    } 
    while (n > 0){
        p = (n % 10) * p; 
        n = n/10; 
    }
    return persistence(p) + 1;
}

int main()
{
    cout << persistence(39) << "\n";
    cout << persistence(4) << "\n";
    cout << persistence(25) << "\n";
    cout << persistence(999) << "\n";
    cout << persistence(444) << "\n"; 
};