#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string fakeBin(string str)
{
    /*
    stringstream ss;
    for (char c: str)
    {
        ss << (int(c) >= 53 ? '1' : '0');
    }
    return ss.str();
    */
    string s;
    transform(str.begin(), str.end(), back_inserter(s),
        [](char c) { return int(c) >= 53 ? '1' : '0'; });
    return s;
}

void That(string q, string a){
    if(q != a){
        cout << "Q: " << q << " |A: " << a << "\n";
        for (int i = 0; i < q.size(); i++)
        {
            cout << "Char: " << q[i] << " | " << a[i] << " " << (q[i] == a[i]) << "\n";
        }
    }
    cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

string Equals(string b){
    return b;
}

int main()
{
    That(fakeBin("45385593107843568"), Equals("01011110001100111"));
    That(fakeBin("509321967506747"), Equals("101000111101101"));
    That(fakeBin("366058562030849490134388085"), Equals("011011110000101010000011011"));
    That(fakeBin("15889923"), Equals("01111100"));
    That(fakeBin("800857237867"), Equals("100111001111"));
}