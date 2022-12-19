#include <vector>
#include <string>
#include <iostream>

using namespace std;

bool check(const vector<string>& seq, const string& elem) {
    return find(begin(seq), end(seq), elem) != end(seq);
}

int main()
{
    cout << check({ },               "a") << "\n";
    cout << check({ "a", "b", "c"},  "b") << "\n";
    cout << check({ "a", "b", "c"},  "e") << "\n";
};