#include "../UnitTest/unitest.hpp"
#include <iostream>
#include <string>

using namespace std;

int strCount(string word, char letter)
{
    return count(word.begin(), word.end(), letter);
}

int main()
{
    unitest t;
    t.That(strCount("Hello", 'o'), t.Equals(1));
    t.That(strCount("Hello", 'l'), t.Equals(2));
    t.That(strCount("Hello", 'q'), t.Equals(0));
    t.That(strCount("Pippi", 'p'), t.Equals(2));
    t.That(strCount("", 'l'), t.Equals(0));
}