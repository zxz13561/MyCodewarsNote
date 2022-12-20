#include <iostream>
#include <string>

using namespace std;

string sliceString(string str)
{
    return str.substr(1, str.size() - 2);
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
    That(sliceString("tuna"), Equals("un"));
    That(sliceString("rats"), Equals("at"));
    That(sliceString("code"), Equals("od"));
    That(sliceString("country"), Equals("ountr"));
    That(sliceString("place"), Equals("lac"));
    That(sliceString("translation"), Equals("ranslatio"));
}