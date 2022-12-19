#include <iostream>

using namespace std;

bool checkForFactor(int base, int factor) {
    return base % factor == 0;
}

void That(bool q, bool a){
    cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

bool Equals(bool b){
    return b;
}

int main()
{
    That(checkForFactor(10, 2), Equals(true));
    That(checkForFactor(63, 7), Equals(true));
    That(checkForFactor(2450, 5), Equals(true));
    That(checkForFactor(24612, 3), Equals(true));
    That(checkForFactor(9, 2), Equals(false));
    That(checkForFactor(653, 7), Equals(false));
    That(checkForFactor(2453, 5), Equals(false));
    That(checkForFactor(24617, 3), Equals(false));
};