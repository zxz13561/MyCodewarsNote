#include <iostream>
#include <cctype>
#include <sstream>

using namespace std;

string accum(const std::string &s){
    string res;
    for(unsigned long i = 0; i < s.size(); i++){
        res += (char)toupper(s[i]) + string(i, (char)tolower(s[i])) + '-';
    }
    res.pop_back();
    return res;
}

string other_one_code(const std::string &s){
    stringstream result;
    for (int i = 0; i < s.length(); i++) 
        result << "-" << string(1, toupper(s[i])) << string(i, tolower(s[i])); 
    return result.str().substr(1);
}

int main()
{
    cout << accum("ZpglnRxqenU") << "\n";
    cout << accum("NyffsGeyylB") << "\n";
};