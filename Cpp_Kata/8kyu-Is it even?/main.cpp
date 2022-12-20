#include "../UnitTest/unitest.hpp"
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

int main()
{
    unitest t;
    t.That(is_even(0),   t.Equals(true));
    t.That(is_even(0.5), t.Equals(false));
    t.That(is_even(1),   t.Equals(false));
    t.That(is_even(2),   t.Equals(true));
    t.That(is_even(-4),  t.Equals(true));
    t.That(is_even(0.88),  t.Equals(false));
    t.That(is_even(1.38),  t.Equals(false));
    t.That(is_even(555555555556),  t.Equals(true));
};