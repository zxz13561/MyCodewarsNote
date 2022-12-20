#include <iostream>
#include <string>
#include "../UnitTest/unitest.hpp"

using namespace std;

string sliceString(string str)
{
    return str.substr(1, str.size() - 2);
}

int main()
{
    unitest t;
    t.That(sliceString("tuna"), t.Equals("un"));
    t.That(sliceString("rats"), t.Equals("at"));
    t.That(sliceString("code"), t.Equals("od"));
    t.That(sliceString("country"), t.Equals("ountr"));
    t.That(sliceString("place"), t.Equals("lac"));
    t.That(sliceString("translation"), t.Equals("ranslatio"));
}