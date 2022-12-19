#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

bool is_even_try(double n)
{
    n = n >= 0 ? n : -n;
    return (long)n == n ? (long)n % 2 == 0 : false;
}

bool is_even(double n)
{
    return fmod(n, 2) == 0;
}

void do_test(double n, bool ans){
    cout << "\nQ: " << n << "\n";
    string res = is_even(n) == ans ? "Pass" : "Fail";
    cout << "Is Correct: " << res << "\n"; 
}

int main()
{
    do_test(0,   true);
    do_test(0.5, false);
    do_test(1,   false);
    do_test(2,   true);
    do_test(-4,  true);
    do_test(0.88,  false);
    do_test(1.38,  false);
    do_test(555555555556,  true);
};